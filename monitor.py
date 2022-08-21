import rtmidi2


# output incoming midi data:
def monitor(midi_port_pick):
    midi_in = rtmidi2.MidiIn()
    #midi_out = rtmidi2.MidiOut()
    midi_in.open_port(int(midi_port_pick))
    while True:
        x = midi_in.get_message()
        if x:
            print("MIDI IN:" , x)


# get available devices ask for input:
in_ports = rtmidi2.get_in_ports()
out_ports = rtmidi2.get_out_ports()
print(in_ports, '\n', out_ports)

midi_choice = input("select device channel")

monitor(midi_choice)  # not sure when to cast to int yet
