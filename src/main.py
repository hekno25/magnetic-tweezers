import serial
import sys

from typing import Iterable

import functools

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)
from PySide6.QtCore import QByteArray, QCoreApplication, QIODevice

from PySide6.QtGui import QAction

from PySide6.QtSerialPort import QSerialPort
import serial.tools.list_ports

from ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Magnetic Tweezer Control")

        self.serial = QSerialPort(self)
        self.serial.readyRead.connect(self.read_serial_data)
        self.com_port = ""

        # Actual target in milliteslas, always reference this rather than
        # the slider or spinbox values
        self.coil_targets = [0.0, 0.0, 0.0, 0.0, 0.0]

        self.coil_inputs = [
            (self.coilSlider1, self.coilSpinBox1, "X"),
            (self.coilSlider2, self.coilSpinBox2, "Y"),
            (self.coilSlider3, self.coilSpinBox3, "Z"),
        ]

        for index, (slider, spinbox, _axis) in enumerate(self.coil_inputs):
            # We provide just the index, QT's signal system will provide the
            # value for the callback
            slider.sliderReleased.connect(
                functools.partial(self.on_slider_released, index)
            )
            spinbox.editingFinished.connect(
                functools.partial(self.on_spinbox_editing_finished, index)
            )
            max_milliteslas = 5

            slider.setMaximum(max_milliteslas * 1000)
            slider.setMinimum(max_milliteslas * -1000)
            spinbox.setMaximum(max_milliteslas)
            spinbox.setMinimum(max_milliteslas * -1)
            spinbox.setSingleStep(0.1)
            spinbox.setSuffix("mT")
            spinbox.setDecimals(3)

            slider.setValue(int(self.coil_targets[index] * 1000))
            spinbox.setValue(self.coil_targets[index])

        self.findPorts()

    def findPorts(self):
        self.ports = sorted(serial.tools.list_ports.comports())
        actions = self.menuSerial.actions()
        existing_ports = []
        for action in actions:
            existing_ports.append(action.text())

        for port in self.ports:
            if port.description in existing_ports or port.description == "n/a":
                continue
            com_port = QAction(port.description, self, checkable=True)
            com_port.setObjectName(port.device)
            com_port.triggered.connect(self.on_serial_connect)
            self.menuSerial.addAction(com_port)
            self.serial.setPortName(port[0])
            self.serial.close()

    def on_serial_connect(self):
        for port in self.menuSerial.actions():
            try:
                if port.isChecked():
                    self.com_port = port.objectName()
                    self.serial.setPortName(self.com_port)
                    self.serial.setBaudRate(QSerialPort.BaudRate(115200))
                    self.serial.setDataBits(QSerialPort.DataBits.Data8)
                    self.serial.setParity(QSerialPort.Parity.NoParity)
                    self.serial.setStopBits(QSerialPort.StopBits.OneStop)
                    self.serial.setFlowControl(QSerialPort.FlowControl.NoFlowControl)

                if (
                    not self.serial.open(QIODevice.OpenModeFlag.ReadWrite)
                    or not port.isChecked()
                ):
                    self.sync = False
                    port.setChecked(False)
                    self.serial.close()
                    print(f"Closed port: {self.com_port}".ljust(200))
                    self.connectionStatus.setText(
                        QCoreApplication.translate(
                            "MainWindow", "Status: Disconnected", None
                        )
                    )
                else:
                    self.connectionStatus.setText(
                        QCoreApplication.translate(
                            "MainWindow", f"Status: Connected to {port.text()}", None
                        )
                    )

            except Exception as e:
                port.setChecked(False)
                self.connectionStatus.setText(
                    QCoreApplication.translate("MainWindow", f"Status: {str(e)}", None)
                )

    def on_spinbox_editing_finished(self, index):
        slider, spinbox, _axis = self.coil_inputs[index]
        slider.setValue(int(spinbox.value() * 1000))
        self.on_slider_released(index)

    def on_slider_released(self, index):
        slider, spinbox, axis = self.coil_inputs[index]
        spinbox.setValue(slider.value() / 1000)

        self.coil_targets[index] = 5

        data = [axis, slider.value() / 1000]
        self.write_serial_data(data)

    def read_serial_data(self):
        try:
            incoming_data = self.serial.readAll().data()
            if not incoming_data:
                return
            print(f"Arduino: {incoming_data}")
        except Exception as e:
            print(f"Error reading serial data: {e}")

    def write_serial_data(self, data: Iterable):
        try:
            formatted_data = str("")
            for item in data:
                formatted_data += f"{item};"
            formatted_data += "\n"
            print(f"Sent data to Arduino: {formatted_data}")

            self.serial.write(formatted_data.encode("utf-8"))
        except Exception as e:
            print(f"Error writing serial data: {e}")

    def calculate_target_voltage(self, target_milliteslas):
        # TODO: Do a real calculation
        return target_milliteslas


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = MainWindow()

    window.show()
    sys.exit(app.exec())
