:orphan:

..
  See
  https://docs.zephyrproject.org/latest/releases/index.html#migration-guides
  for details of what is supposed to go into this document.

.. _migration_4.2:

Migration guide to Zephyr v4.2.0 (Working Draft)
################################################

This document describes the changes required when migrating your application from Zephyr v4.1.0 to
Zephyr v4.2.0.

Any other changes (not directly related to migrating applications) can be found in
the :ref:`release notes<zephyr_4.2>`.

.. contents::
    :local:
    :depth: 2

Build System
************

Kernel
******

Boards
******

* All boards based on Nordic ICs that used the ``nrfjprog`` Nordic command-line
  tool for flashing by default have been modified to instead default to the new
  nRF Util (``nrfutil``) tool. This means that you may need to `install nRF Util
  <https://www.nordicsemi.com/Products/Development-tools/nrf-util>`_ or, if you
  prefer to continue using ``nrfjprog``, you can do so by invoking west while
  specfying the runner: ``west flash -r nrfjprog``. The full documentation for
  nRF Util can be found
  `here <https://docs.nordicsemi.com/bundle/nrfutil/page/README.html>`_.

* The config option :kconfig:option:`CONFIG_NATIVE_POSIX_SLOWDOWN_TO_REAL_TIME` has been deprecated
  in favor of :kconfig:option:`CONFIG_NATIVE_SIM_SLOWDOWN_TO_REAL_TIME`.

* Zephyr now supports version 1.11.1 of the :zephyr:board:`neorv32`.

* ``arduino_uno_r4_minima``, ``arduino_uno_r4_wifi``, and ``mikroe_clicker_ra4m1`` have migrated to
  new FSP-based configurations.
  While there are no major functional changes, the device tree structure has been significantly revised.
  The following device tree bindings are now removed:
  ``renesas,ra-gpio``, ``renesas,ra-uart-sci``, ``renesas,ra-pinctrl``,
  ``renesas,ra-clock-generation-circuit``, and ``renesas,ra-interrupt-controller-unit``.
  Instead, use the following replacements:
  - :dtcompatible:`renesas,ra-gpio-ioport`
  - :dtcompatible:`renesas,ra-sci-uart`
  - :dtcompatible:`renesas,ra-pinctrl-pfs`
  - :dtcompatible:`renesas,ra-cgc-pclk-block`

Device Drivers and Devicetree
*****************************

DAI
===

* Renamed the devicetree property ``dai_id`` to ``dai-id``.
* Renamed the devicetree property ``afe_name`` to ``afe-name``.
* Renamed the devicetree property ``agent_disable`` to ``agent-disable``.
* Renamed the devicetree property ``ch_num`` to ``ch-num``.
* Renamed the devicetree property ``mono_invert`` to ``mono-invert``.
* Renamed the devicetree property ``quad_ch`` to ``quad-ch``.
* Renamed the devicetree property ``int_odd`` to ``int-odd``.

Counter
=======

* ``counter_native_posix`` has been renamed ``counter_native_sim``, and with it its
  kconfig options and DT binding. :dtcompatible:`zephyr,native-posix-counter`  has been deprecated
  in favor of :dtcompatible:`zephyr,native-sim-counter`.
  And :kconfig:option:`CONFIG_COUNTER_NATIVE_POSIX` and its related options with
  :kconfig:option:`CONFIG_COUNTER_NATIVE_SIM` (:github:`86616`).

Entropy
=======

* ``fake_entropy_native_posix`` has been renamed ``fake_entropy_native_sim``, and with it its
  kconfig options and DT binding. :dtcompatible:`zephyr,native-posix-rng`  has been deprecated
  in favor of :dtcompatible:`zephyr,native-sim-rng`.
  And :kconfig:option:`CONFIG_FAKE_ENTROPY_NATIVE_POSIX` and its related options with
  :kconfig:option:`CONFIG_FAKE_ENTROPY_NATIVE_SIM` (:github:`86615`).

Ethernet
========

* Removed Kconfig option ``ETH_STM32_HAL_MII`` (:github:`86074`).
  PHY interface type is now selected via the ``phy-connection-type`` property in the device tree.

GPIO
====

* To support the RP2350B, which has many pins, the RaspberryPi-GPIO configuration has
  been changed. The previous role of :dtcompatible:`raspberrypi,rpi-gpio` has been migrated to
  :dtcompatible:`raspberrypi,rpi-gpio-port`, and :dtcompatible:`raspberrypi,rpi-gpio` is
  now left as a placeholder and mapper.
  The labels have also been changed along, so no changes are necessary for regular use.

Bluetooth
*********

Bluetooth Host
==============

* The symbols ``BT_LE_CS_TONE_ANTENNA_CONFIGURATION_INDEX_<NUMBER>`` in
  :zephyr_file:`include/zephyr/bluetooth/conn.h` have been renamed
  to ``BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A<NUMBER>_B<NUMBER>``.

Networking
**********

* The struct ``net_linkaddr_storage`` has been renamed to struct
  :c:struct:`net_linkaddr` and the old struct ``net_linkaddr`` has been removed.
  The struct :c:struct:`net_linkaddr` now contains space to store the link
  address instead of having pointer that point to the link address. This avoids
  possible dangling pointers when cloning struct :c:struct:`net_pkt`. This will
  increase the size of struct :c:struct:`net_pkt` by 4 octets for IEEE 802.15.4,
  but there is no size increase for other network technologies like Ethernet.
  Note that any code that is using struct :c:struct:`net_linkaddr` directly, and
  which has checks like ``if (lladdr->addr == NULL)``, will no longer work as expected
  (because the addr is not a pointer) and must be changed to ``if (lladdr->len == 0)``
  if the code wants to check that the link address is not set.

SPI
===

* Renamed the device tree property ``port_sel`` to ``port-sel``.
* Renamed the device tree property ``chip_select`` to ``chip-select``.

Other subsystems
****************

Modules
*******

Architectures
*************
