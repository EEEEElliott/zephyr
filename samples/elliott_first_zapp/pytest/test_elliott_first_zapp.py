from twister_harness import DeviceAdapter

def test_log(dut: DeviceAdapter):
   dut.readlines_until('Hello Elliott!')
   dut.readlines_until('This is your first zephyr app!')
   dut.readlines_until('LED is going to blink!')
   dut.readlines_until('LED state: ON')
   dut.readlines_until('LED state: OFF')