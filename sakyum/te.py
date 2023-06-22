import os

class BaseStructure:
    """base structure class"""

    def __init__(self, is_software=True):
        """base structure class initializer"""
        self.is_software = is_software
        self.fls_cmd = 'echo. >'
        self._exs_first = ['index']
        self._exs_last = ['.html']

    def create_files(self, directory):
        """Create files with specified names and extensions"""
        os.makedirs(directory, exist_ok=True)
        for name in self._exs_first:
            for extension in self._exs_last:
                file_path = os.path.join(directory, f"{name}{extension}")
                os.system(f"{self.fls_cmd} {file_path}")
                with open(f"{file_path}", 'w') as pay_fls:
                  pay_fls.write(f'aswdfrgthyju')

BaseStructure().create_files('sgs')
