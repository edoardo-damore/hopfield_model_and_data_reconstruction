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
  """
  `corruption_type` lets you chose the type of corruption applied to `patterns`:
  - "Flip": flips each bit with probability `q`
  - "Erase": sets a fraction `q` of the bits to -1
  - "ImErase": treats the single pattern as an image, setting a fraction `~q` of its bits starting from the bottom. 
  The pattern lenght must be a perfect square
  """
  try:
    assert q >= 0 and q <= 1
  except:
    print("q must have a value between 0 and 1 (included)")
    return
  
  match corruption_type:
    case "Flip":
      corrupted = patterns.copy()
      for p in corrupted:
        choice = np.random.choice([0,1], size=p.shape, p=[1-q, q])
        p[:] = np.where(choice == 0, p, -p)
      return corrupted
    
    case "Erase":
      corrupted = patterns.copy()
      threshold = int(np.floor(corrupted.shape[1] * (1-q)))
      corrupted[:,threshold:] = -1
      return corrupted
    
    case "ImErase":
      try:
        assert np.allclose(np.sqrt(patterns.shape[1]) % 1, 0)
      except:
        print("Pattern lenght is not a perfect square!")
        return

      corrupted = patterns.copy()
      l = int(np.sqrt(corrupted.shape[1]))
      threshold = int(l * (1-q))
      for p in corrupted:
        p.reshape(l,l)[threshold:] = -1
      return corrupted
    case _:
      print("Please select a valid corruption_type")
      return
    

def maximum_recall(pattern_lenght: int, degree: int):
  """
  Returns the expected number of patterns a modern hopfield network of size `pattern_lenght` 
  whose energy functions is a polynomial of order `degree` can recall
  """
  return pattern_lenght**(degree - 1) / (2 * _double_factorial(2 * degree - 3) * np.log(pattern_lenght)) 

def _double_factorial(N: int):
  if N > 0:
    return N * _double_factorial(N - 2)
  else:
    return 1



def visualize_patterns(patterns: np.ndarray):
  pass