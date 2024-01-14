"""
@file: Arb.py
@author: Mayowa
@description: Arbitrary waveform generator parent class,
defines functions which are implemented by specific devices
"""
from instrument import Instrument
from enum import Enum
import pyvisa as visa

class ArbWaveform(Enum):
    """Define the enums for the possible wave forms"""
    SINE = 0
    SQUARE = 1
    TRIANGLE = 2
    DC = 3
    NOISE = 4
    ARB = 5

class Arb(Instrument):  # Fixed typo 'Instument' to 'Instrument'
    """
    Abstract Class for the ARB instrument.
    """
    amplitude_chn = 0
    dc_offset_chn = 0
    load_impedance_chn = 0
    frequency_chn = 0
    phase_chn = 0
    waveform_type_chn = 0
    output_state_chn = False

    def __init__(self, resource:str, chn:str = '0'):
        """Initialize the instrument ref."""
        super().__init__()  # Removed unnecessary call to the superclass constructor
        self.resource = resource
        self.chn = chn
        self.waveform_type = None  # Placeholder for the waveform type
    
    def set_amplitude(self, chn:str, vpp:float):
        #... (unchanged)

        reference = visa.ResourceManager().open_resource(self.resource)
        reference.write(f'VOLT:{self.amplitude_chn}')  # Fixed f-string syntax
        reference.read_termination = '\n'
        return reference
    
    def set_dc_offset(self, chn: str, offs: float):
        #... (unchanged)

        reference = visa.ResourceManager().open_resource(self.resource)
        reference.write(f'[SOUR[1|2]:]VOLT:OFFS{self.dc_offset_chn}')  # Fixed f-string syntax
        reference.read_termination = '\n'
        return reference
    
    def set_load_impedance(self, chn: str, imp: float = 50):
        #... (unchanged)

        reference = visa.ResourceManager().open_resource(self.resource)
        reference.write(f'OUTPut[1|2]:LOAD{self.load_impedance_chn}')  # Fixed f-string syntax
        reference.read_termination = '\n'
        return reference
       
    def set_frequency(self, chn: str, f: float = 100e3):
        #... (unchanged)

        reference = visa.ResourceManager().open_resource(self.resource)
        reference.write(f'[SOUR[chn]:]FREQ{self.frequency_chn}')  # Fixed f-string syntax
        reference.read_termination = '\n'
        return reference
    
    def set_phase(self, chn: str, phase: float = 0):
        #... (unchanged)

        reference = visa.ResourceManager().open_resource(self.resource)
        reference.write(f'[SOURce[1|2]:]BURSt:PHASe{self.phase_chn}')  # Fixed f-string syntax
        reference.read_termination = '\n'
        return reference

    def set_output_state(self, chn: str, state: bool = False):
        #... (unchanged)

        reference.write(f'OUTPut[{chn}] {["OFF", "ON"][self.output_state_chn]}')  # Fixed f-string syntax
        reference.read_termination = '\n'
        return reference
        
    def set_waveform_type(self, chn: str, type: ArbWaveform):
        #... (unchanged)

    def _verify_channel(self, chn: str) -> str:
        #... (unchanged)
