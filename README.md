This repository contains code for interfacing with a remoted LoRa antenna.

## Structure
- ``/change_address.py`` contains the code for adjusting the address of the remoted LoRa reciever with [AT commands](https://reyax.com/upload/products_download/download_file/LoRa-AT-Command-RYLR40x_RYLR89x_EN-8.pdf).
- ``/client.py`` contains the code for adjusting the transmitting frequency and the sampling frequency of the remoted LoRa antenna.
- ``/proxy.py`` contains code for communicating with the remoted LoRa antenna with AT commands.
- ``/server.py`` contains code for mimicing a VOLTTRON instance that serves as a hub.

## Quick-Start
1) In a separate terminal, run ``/server.py``
2) In a separate terminal, run ``/proxy.py``
    * Replace ``74`` in line 32 with the address of the remoted LoRa reciever 
3) In a separate terminal, run ``/client.py`` to change the transmitting frequency and the sampling frequency