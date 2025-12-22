from dataclasses import dataclass

@dataclass
class Main:
    kw_arg1: str  
    kw_arg2: str
    kw_arg3: str

class MainSuper(Main):
    pass

lazy1 = Main(kw_arg1='arg1', kw_arg2='arg2', kw_arg3='arg3')

lazy2 = Main(kw_arg1='arg1', kw_arg2='arg2', kw_arg3='arg3')

print(lazy1.kw_arg1)

print(lazy1.kw_arg2)

@dataclass
class Main:
  kw_arg1: str  
  kw_arg2: str
  kw_arg3: str
  kw_arg4: str  
  kw_arg5: str
  kw_arg6: str
