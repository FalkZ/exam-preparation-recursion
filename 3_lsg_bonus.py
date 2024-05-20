# Text Aufgabe: Was braucht es zum folgende Statements auch darzustellen: ((2 + 3) * 4) oder (1 * ((2 + 4) + 3))

# Muss etwas am Code geändert werden? Wenn ja, was?

# A: Anstatt dass man als left und right Zahlen übergibt bei der Instanzierung der Klasse, kann man auch Statements übergeben.
# (Die to_string Methode muss so geändert werden, dass falls left oder right Statements sind, auf denen auch die to_string Methode aufgerufen wird.)

# Erstelle Instanzen der beiden Statements darzustellen

# ((2 + 3) * 4)
# Statement(Statement(2, "+", 3), "*", 4))

# (1 * ((2 + 4) + 3))
# Statement(1, "*", Statement(Statement(2, "+", 4), "+", 3))
