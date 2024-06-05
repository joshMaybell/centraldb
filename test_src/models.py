"""Module providing database models for influxdb."""

import abc
import datetime
import enum
from typing import Any, Literal, Tuple, Type
import typing

import influxdb_client
import influxdb_client.client
import influxdb_client.client.write.point
import influxdb_client.client.write_api
import influxdb_client.domain
import pydantic

SupportedType = Literal[
    "bga",
    "compressor",
    "ecodry",
    "flow",
    "heater",
    "inverter",
    "pressure",
    "pump",
    "thermometer",
    "trap",
    "turbo",
    "valve",
]

SUPPORTED_TYPES: Tuple[SupportedType, ...] = typing.get_args(SupportedType)


def model_from_type(model_type: SupportedType):
    """Return the db model corresponding to the given type."""

    target: Type[pydantic.BaseModel] | None = None
    match model_type:
        case "bga":
            target = Bga
        case "compressor":
            target = Compressor
        case "ecodry":
            target = Ecodry
        case "flow":
            target = Flow
        case "heater":
            target = Heater
        case "inverter":
            target = Inverter
        case "pressure":
            target = Pressure
        case "pump":
            target = Pump
        case "thermometer":
            target = Thermometer
        case "trap":
            target = Trap
        case "turbo":
            target = Turbo
        case "valve":
            target = Valve

    return target


class Model(pydantic.BaseModel):
    """Generic db model for influxdb data entries."""

    _type: str
    _tag: str

    # Name should not be dumped.
    name: str = pydantic.Field(exclude=True)

    def as_point(self, time: str | None = None):
        """Return the model represented as an influxdb Point."""
        if time is None:
            time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        point = influxdb_client.client.write.point.Point(measurement_name=self._type)
        point.time(time)
        point.tag(self._tag, self.name)

        for key, value in self.model_dump().items():
            if isinstance(value, enum.Enum):
                point.field(key, value.name)
            else:
                point.field(key, value)

        return point

    @classmethod
    @abc.abstractmethod
    def from_value(cls, name: str, value: Any | dict[str, Any]) -> "Model":
        # pylint: disable=unused-argument
        """Create a new model from its native value."""
        ...


class Thermometer(Model):
    """Model for thermometer sensor devices."""

    _type: str = "thermometer"
    _tag: str = "sensor"

    temperature: float | None
    resistance: float | None
    quadrature: float | None

    @classmethod
    def from_value(cls, name: str, value: dict[str, Any] | None):
        """Create a thermometer object from a dictionary.

        `values` should contain keys for "temperature", "resistance", and "quadrature".
        If `values` is None, returns a null-valued thermometer object.
        """
        if value is None:
            return Thermometer(
                name=name,
                temperature=None,
                resistance=None,
                quadrature=None,
            )
        return Thermometer(name=name, **value)


class Pressure(Model):
    """Model for pressure gauge devices."""

    _type: str = "pressure"
    _tag: str = "sensor"

    pressure: float | None

    @classmethod
    def from_value(cls, name: str, value: float | dict[str, float] | None):
        """Create a pressure object from a dictionary.

        `values` can be either a float or a dict.
        If `value` is a float, the pressure field is set to `value`
        If `value` is a dict, the pressure field is set to value of "pressure".
        If `values` is None, returns a null-valued pressure object.
        """

        if isinstance(value, dict):
            return Pressure(name=name, pressure=value.get("pressure"))

        return Pressure(name=name, pressure=value)


class Bga(Model):
    """Model for bga devices."""

    _type: str = "bga"
    _tag: str = "sensor"

    percent: float | None

    @classmethod
    def from_value(cls, name: str, value: float | dict[str, float] | None):
        """Create a percent object from a dictionary.

        `values` can be either a float or a dict.
        If `value` is a float, the percent field is set to `value`
        If `value` is a dict, the pressure field is set to value of "percent".
        If `values` is None, returns a null-valued percent object.
        """

        if isinstance(value, dict):
            return Bga(name=name, percent=value.get("percent"))

        return Bga(name=name, percent=value)


class Flow(Model):
    """Model for Turbo devices.

    This model is designed to support Flowmeter devices using the lib/alicat interface.
    """

    _type: str = "flow"
    _tag: str = "sensor"

    pressure: float | None
    temperature: float | None
    volumetric_flow: float | None
    mass_flow: float | None

    @classmethod
    def from_value(cls, name: str, value: dict[str, Any] | None):
        """Create a flow object from a dictionary.

        `values` can be either a float or a dict.
        If `value` is a float, the flow field is set to `value`
        If `value` is a dict, the flow field is set to value of "flow".
        If `values` is None, returns a null-valued flow object.
        """

        if value is None:
            return Flow(
                name=name,
                pressure=None,
                temperature=None,
                volumetric_flow=None,
                mass_flow=None,
            )

        return Flow(name=name, **value)


class Valve(Model):
    """Model for valve device."""

    _type: str = "valve"
    _tag: str = "device"

    open: bool | None

    @classmethod
    def from_value(cls, name: str, value: bool | dict[str, bool] | None):
        """Create a valve object from a dictionary.

        `values` can be either a bool or a dict.
        If `value` is a float, the valve field is set to `value`
        If `value` is a dict, the valve field is set to value of "open".
        If `values` is None, returns a null-valued valve object.
        """

        if isinstance(value, dict):
            return Valve(name=name, open=value.get("open"))

        return Valve(name=name, open=value)


class Trap(Model):
    """Model for trap devices with pwm output."""

    _type: str = "trap"
    _tag: str = "device"

    output: float | None

    @classmethod
    def from_value(cls, name: str, value: float | dict[str, float] | None):
        """Create a trap object from a dictionary.

        `value` can be either a float or a dict.
        If `value` is a float, the trap output field will be set to `value`
        If `value` is a dict, the trap output field will be set to the value of `output`
        If `value` is None, returns a null-valued trap object.
        """

        if isinstance(value, dict):
            return Trap(name=name, output=value.get("output"))

        return Trap(name=name, output=value)


class Pump(Model):
    """Model for on/off pump devices."""

    _type: str = "pump"
    _tag: str = "device"

    active: bool | None

    @classmethod
    def from_value(cls, name: str, value: bool | dict[str, bool] | None):
        """Create a pump object from a dictionary.

        `values` can be either a bool or a dict.
        If `value` is a float, the pump field is set to `value`
        If `value` is a dict, the pump field is set to value of "active".
        If `values` is None, returns a null-valued pump object.
        """

        if isinstance(value, dict):
            return Pump(name=name, active=value.get("active"))

        return Pump(name=name, active=value)


class Heater(Model):
    """Model for heater devices."""

    _type: str = "heater"
    _tag: str = "device"

    power: float | None
    current: float | None
    voltage: float | None
    native: float | None

    @classmethod
    def from_value(cls, name: str, value: dict[str, float] | float | None):
        """Create a heater object from a dictionary.

        `values` can be either a float or a dict.
        If `value` is a float, the heater field is set to `value`
        If `value` is a dict, the heater field is set to value of "power".
        If `values` is None, returns a null-valued heater object.
        """

        if value is None:
            return Heater(
                name=name,
                power=None,
                current=None,
                voltage=None,
                native=None,
            )

        if isinstance(value, (float | int)):
            return Heater(
                name=name, power=value, current=None, voltage=None, native=None
            )

        return Heater(
            name=name,
            power=value.get("power"),
            current=value.get("current"),
            voltage=value.get("voltage"),
            native=value.get("native"),
        )


class Turbo(Model):
    """Model for Turbo devices.

    This model is designed to support Turbo devices using the lib/turbovac interface.
    """

    _type: str = "turbo"
    _tag: str = "device"

    state: bool | None
    speed: int | None
    converter: int | None
    motor: int | None
    bearing: int | None
    setpoint: int | None
    voltage: int | None
    error: bool | None

    @classmethod
    def from_value(cls, name: str, value: dict[str, Any] | None):
        """Create a turbo object from a dictionary.

        `values` should contain keys for "state", "speed", "converter", "motor",
        "bearing", "setpoint", and "voltage".
        If `values` is None, returns a null-valued turbo object.
        """
        if value is None:
            return Turbo(
                name=name,
                state=None,
                speed=None,
                converter=None,
                motor=None,
                bearing=None,
                setpoint=None,
                voltage=None,
                error=None,
            )
        return Turbo(name=name, **value)


class Ecodry(Model):
    """Model for Ecodry devices.

    This model is designed to support Turbo devices using the lib/ecodry interface.
    """

    _type: str = "ecodry"
    _tag: str = "device"

    setpoint: float | None
    frequency: float | None
    current: float | None
    voltage: float | None
    bus_voltage: float | None
    power: float | None
    state: bool | None

    @classmethod
    def from_value(cls, name: str, value: dict[str, Any] | None):
        """Create a ecodry object from a dictionary.

        `values` should contain keys for "setpoint", "frequency", "current", "voltage",
        "bus_voltage", "power", and "state".
        If `values` is None, returns a null-valued ecodry object.
        """
        if value is None:
            return Ecodry(
                name=name,
                setpoint=None,
                frequency=None,
                current=None,
                voltage=None,
                bus_voltage=None,
                power=None,
                state=None,
            )
        return Ecodry(name=name, **value)


class Inverter(Model):
    """Model for Inverter devices.

    This model is designed to support Turbo devices using the lib/inverter interface.
    """

    _type: str = "inverter"
    _tag: str = "device"

    state: bool | None
    frequency: float | None
    current: float | None
    voltage: float | None
    alarm: str | None

    @classmethod
    def from_value(cls, name: str, value: dict[str, Any] | None):
        """Create a inverter object from a dictionary.

        `values` should contain keys for "state", "frequency", "current", "voltage",
        and "alarm"
        If `values` is None, returns a null-valued inverter object.
        """
        if value is None:
            return Inverter(
                name=name,
                state=None,
                frequency=None,
                current=None,
                voltage=None,
                alarm=None,
            )
        return Inverter(name=name, **value)


class Compressor(Model):
    """Model for Compressor devices.

    This model is designed to support Turbo devices using the lib/f70 interface.
    """

    _type: str = "compressor"
    _tag: str = "device"

    state: bool | None
    discharge_temperature: float | None
    outlet_temperature: float | None
    inlet_temperature: float | None
    return_pressure: float | None

    @classmethod
    def from_value(cls, name: str, value: dict[str, Any] | None):
        """Create a inverter object from a dictionary.

        `values` should contain keys for "discharge_temperature", "frequency",
        "outlet_temperature", "inlet_temperature", and "return_pressure".
        If `values` is None, returns a null-valued inverter object.
        """
        if value is None:
            return Compressor(
                name=name,
                state=None,
                discharge_temperature=None,
                outlet_temperature=None,
                inlet_temperature=None,
                return_pressure=None,
            )
        return Compressor(name=name, **value)
