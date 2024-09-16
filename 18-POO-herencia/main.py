import clases

persona = clases.Persona()
persona.setNombre("Víctor")
persona.setApellidos("Vergara")
persona.setAltura("170cm")
persona.setEdad("800 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())