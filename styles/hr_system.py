with open("styles/hr_system.txt") as file:
    next(file)  # Saltar la primera línea (encabezado)

    for line in file:
        parts = line.split()

        name = parts[0]
        id_number = parts[1]
        job_title = parts[2]
        salary = float(parts[3])

        # Calcular pago quincenal
        pay = salary / 24

        # Agregar bono si es Engineer
        if job_title == "Engineer":
            pay += 1000

        # Mostrar resultado
        print(f"{name} (ID: {id_number}), {job_title} - ${pay:.2f}")
