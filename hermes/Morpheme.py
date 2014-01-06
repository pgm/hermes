class Morpheme:
  def __init__(self, string, id=0):
    self.__dict__.update(locals())

class NonTerminal(Morpheme):
  def __init__(self, string, id=0, generated=False, macro=None):
    self.__dict__.update(locals())
    super().__init__(string, id)
  def id(self):
    return self.id
  def setMacro(self, macro):
    self.macro = macro
  def str(self, theme=None):
    return self.__str__(theme)
  def __str__(self, theme=None):
    return theme.nonterminal(self.string) if theme else self.string
  def first(self):
    return 

class Terminal(Morpheme):
  def __init__(self, string, id=0):
    super().__init__(string, id)
    self.isSeparator = False
  def id(self):
    return self.id
  def str(self, theme=None):
    return self.__str__(theme)
  def __str__(self, theme=None):
    return theme.terminal("'" + self.string + "'") if theme else "'" + self.string + "'"
  def first(self):
    return {self}

class AbstractTerminal(Terminal):
  pass

class EmptyString(AbstractTerminal):
  def __init__(self, id):
    super().__init__('ε', id)
  def str(self, theme=None):
    return self.__str__(theme)
  def __str__(self, theme=None):
    return theme.emptyString('ε') if theme else 'ε'

class EndOfStream(AbstractTerminal):
  def __init__(self, id):
    super().__init__('σ', id)
  def str(self, theme=None):
    return self.__str__(theme)
  def __str__(self, theme=None):
    return theme.endOfStream('σ') if theme else 'σ'
