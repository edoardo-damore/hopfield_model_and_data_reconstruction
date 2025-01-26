import numpy as np
import matplotlib.pyplot as plt


def generate_patterns(pattern_lenght: int, N: int):
  """
  `pattern_lenght`: how many bits is each pattern long \n
  `N`: number of patterns generated \n
  Returns a ndarray of shape (`N`, `pattern_lenght`) containing in each of its rows a different casual pattern
  """
  return np.random.randint(0, 2, size=(N, pattern_lenght)) * 2 - 1

def corrupt_patterns(patterns: np.ndarray, corruption_type: str = "Flip", q: float = 0.1):
  try:
    assert q >= 0 and q <= 1
  except:
    print("q must have a value between 0 and 1 (included)")
    return
  
  match corruption_type:
    case "Flip":
      corrupted = patterns.copy()
      for p in corrupted:
        choice = np.random.choice([0,1], size=p.shape[0], p=[q, 1-q])
        p = np.where(choice == 0, p, -p)
      return corrupted
    case "Erase":
      corrupted = patterns.copy()
      threshold = int(np.floor(corrupted.shape[1] * q))
      corrupted[:,threshold:] = 0
      return corrupted
    case _:
      print("Please select a valid corruption_type")
      return
    



def visualize_patterns(patterns: np.ndarray):
  pass