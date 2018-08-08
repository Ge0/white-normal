import asyncio


class WhiteNormalServerProtocol(asyncio.Protocol):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._video_inputs = 8
        self._video_outputs = 16
        self._monitoring_outputs = 8
        self._serial_ports = 2

    def _send_line(self, line):
        self.transport.write(f"{line}\n")

    def send_preamble(self):
        self._send_line("PROTOCOL PREAMBLE:")
        self._send_line("Version: 2.3")
        self._send_line("")

    def send_device_information(self):
        self._send_line("VIDEOHUB DEVICE:")
        self._send_line("Device present: true")
        self._send_line("Model name: Whitenormal Dumb Videohub")
        self._send_line(f"Video inputs: {self._video_inputs}")
        self._send_line("Video processing units: 0")
        self._send_line(f"Video outputs: {self._video_outputs}")
        self._send_line(
            f"Video monitoring outputs: {self._monitoring_outputs}")
        self._send_line("Serial ports: {self._serial_ports}")
        self._send_line("")

    def send_initial_status(self):
        self._send_line("INPUT_LABELS:")
        for i in range(self._video_inputs):
            self._send_line(f"{i} VTR {i+1}")
        self._send_line("")

        self._send_line("OUTPUT LABELS:")
        for i in range(self._video_outputs):
            self._send_line(f"{i} Output feed {i+1}")
        self._send_line("")

        self._send_line("MONITORING OUTPUT LABELS:")
        for i in range(self._video_outputs):
            self._send_line(f"{i} Mo {i+1}")
        self._send_line("")

        self._send_line("SERIAL PORT LABELS:")
        for i i range(self._serial_ports):
            self._send_line(f"{i} Deck {i+1}")
        self._send_line("")

    def connection_made(self, transport):
        self.transport = transport
        self._send_preamble()
        self._send_device_information()
