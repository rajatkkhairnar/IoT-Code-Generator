import io
from django.shortcuts import render
from django.http import HttpResponse

# Device lists
SENSORS = [
    'DHT11', 'PIR', 'DoorContact', 'Light', 'MQ-2',
    'Ultrasonic', 'SoilMoisture', 'Gas', 'Temperature', 'Humidity'
]
ACTUATORS = [
    'RelayLight', 'SmartPlug', 'ServoLock', 'RGBLED', 'Fan'
]
PINS = [f'Pin{i}' for i in range(6)]


def index(request):
    """
    GET: render form. POST: generate MicroPython script.
    """
    script = None

    if request.method == 'POST':
        # Read network & MQTT settings
        ssid = request.POST.get('ssid')
        password = request.POST.get('password')
        mqtt_host = request.POST.get('mqtt_host')
        mqtt_port = request.POST.get('mqtt_port')
        mqtt_topic = request.POST.get('mqtt_topic')

        # Read device entries
        sensor_types = request.POST.getlist('sensor_type')
        sensor_pins  = request.POST.getlist('sensor_pin')
        intervals    = request.POST.getlist('interval')
        act_types = request.POST.getlist('act_type')
        act_pins  = request.POST.getlist('act_pin')
        triggers  = request.POST.getlist('trigger')

        # Build script
        buf = io.StringIO()
        buf.write('# Auto-generated Smart Home MicroPython script\n')
        buf.write('import network\n')
        if mqtt_host:
            buf.write('import umqtt.simple as mqtt\n')
        buf.write('\n# Connect to Wi-Fi\n')
        buf.write('wifi = network.WLAN(network.STA_IF)\n')
        buf.write('wifi.active(True)\n')
        buf.write(f'wifi.connect("{ssid}", "{password}")\n')

        if mqtt_host:
            buf.write(f'client = mqtt.MQTTClient("client", "{mqtt_host}", port={mqtt_port})\n')
            buf.write('client.connect()\n')

        buf.write('\n# Sensor initialization\n')
        for t,p,i in zip(sensor_types, sensor_pins, intervals):
            buf.write(f'# {t} on {p}, interval={i}s\n')
            buf.write(f'# sensor = {t}.Sensor("{p}")\n')

        buf.write('\n# Actuator initialization\n')
        for t,p,tr in zip(act_types, act_pins, triggers):
            buf.write(f'# {t} on {p}, trigger={tr}\n')
            buf.write(f'# act = {t}.Actuator("{p}")\n')

        buf.write('\n# Main loop\n')
        buf.write('while True:\n')
        buf.write('    # read sensors, publish, listen, control actuators\n')
        buf.write('    pass\n')
        script = buf.getvalue()

    return render(request, 'generator/index.html', {
        'sensors': SENSORS,
        'actuators': ACTUATORS,
        'pins': PINS,
        'script': script,
    })