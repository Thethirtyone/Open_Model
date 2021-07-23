# Function to load and save data into pickles
import pickle
import os


def pickle_it(action='load', filename=None, data=None):
    home_path = os.path.dirname(os.path.abspath(__file__))
    filename = 'save/' + filename
    filename = os.path.join(home_path, filename)
    if action == 'delete':
        try:
            os.remove(filename)
            return ('deleted')
        except Exception:
            return ('failed')

    if action == 'load':
        try:
            with open(filename, 'rb') as handle:
                ld = pickle.load(handle)
                return (ld)
        except Exception:
            return ("file not found")
    else:
        with open(filename, 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
            return ("saved")


def make_safe_filename(s):
    def safe_char(c):
        if c.isalnum():
            return c
        else:
            return "_"

    return "".join(safe_char(c) for c in s).rstrip("_")
