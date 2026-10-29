from django.core.management.base import BaseCommand
from catalogo.models import Juego

class Command(BaseCommand):
    help = 'Carga o actualiza los 18 juegos oficiales de Pixel-Vault'

    def handle(self, *args, **kwargs):
        juegos_data = [
            {"nombre": "Alan Wake 2", "plataforma": "PC / PS5 / Xbox", "precio": 59.99, "descripcion": "Un thriller psicológico de supervivencia en el que una serie de asesinatos rituales amenazan un pueblo idílico.", "imagen": "13"},
            {"nombre": "Baldur's Gate 3", "plataforma": "PC / PS5", "precio": 69.99, "descripcion": "Reúne a tu grupo y regresa a los Reinos Olvidados en un cuento de romances y traición, supervivencia y sacrificio.", "imagen": "7"},
            {"nombre": "Cyberpunk 2077: Ultimate Edition", "plataforma": "PC / PS5 / Xbox", "precio": 69.99, "descripcion": "RPG de acción en mundo abierto ambientado en Night City, incluyendo la expansión Phantom Liberty.", "imagen": "2"},
            {"nombre": "Dead Space Remake", "plataforma": "PC / PS5 / Xbox", "precio": 59.99, "descripcion": "El clásico de terror y ciencia ficción regresa, reconstruido desde cero para ofrecer una experiencia inmersiva.", "imagen": "17"},
            {"nombre": "Elden Ring", "plataforma": "PC / PS5 / Xbox", "precio": 59.99, "descripcion": "Un vasto mundo de fantasía oscura creado por Hidetaka Miyazaki y George R.R. Martin.", "imagen": "5"},
            {"nombre": "Forza Horizon 5", "plataforma": "Xbox / PC", "precio": 59.99, "descripcion": "Tu aventura Horizon definitiva te espera. Explora los vibrantes paisajes del mundo abierto de México.", "imagen": "8"},
            {"nombre": "God of War Ragnarök", "plataforma": "PS5 / PS4", "precio": 69.99, "descripcion": "Kratos y Atreus deben viajar a cada uno de los nueve reinos en busca de respuestas ante la batalla profetizada.", "imagen": "3"},
            {"nombre": "Grand Theft Auto V", "plataforma": "PC / Consolas", "precio": 39.99, "descripcion": "Explora el impresionante mundo abierto de Los Santos y el condado de Blaine en esta experiencia aclamada.", "imagen": "10"},
            {"nombre": "Hades II", "plataforma": "PC / Consolas", "precio": 29.99, "descripcion": "Lucha más allá del Inframundo usando la brujería oscura en esta secuela del aclamado roguelike.", "imagen": "19"},
            {"nombre": "Halo Infinite", "plataforma": "Xbox / PC", "precio": 49.99, "descripcion": "La legendaria saga de Halo regresa con la campaña del Jefe Maestro más extensa hasta la fecha.", "imagen": "4"},
            {"nombre": "Hollow Knight", "plataforma": "PC / Consolas", "precio": 14.99, "descripcion": "Baja bajo la superficie a un vasto reino en ruinas de insectos y héroes en este épico metroidvania.", "imagen": "16"},
            {"nombre": "Metroid Dread", "plataforma": "Nintendo Switch", "precio": 59.99, "descripcion": "Únete a la cazarrecompensas Samus Aran mientras escapa de un letal peligro en el planeta ZDR.", "imagen": "14"},
            {"nombre": "Monster Hunter Rise", "plataforma": "PC / Consolas", "precio": 39.99, "descripcion": "Enfréntate a monstruos imponentes y usa tus recompensas para fabricar un vasto arsenal de armas.", "imagen": "15"},
            {"nombre": "Resident Evil 4 Remake", "plataforma": "PC / PS5 / Xbox", "precio": 59.99, "descripcion": "La supervivencia es solo el comienzo en esta reinvención total del clásico de terror y acción.", "imagen": "11"},
            {"nombre": "Spider-Man 2", "plataforma": "PS5", "precio": 69.99, "descripcion": "Los Spider-Men, Peter Parker y Miles Morales, regresan para una nueva aventura en el universo Marvel.", "imagen": "9"},
            {"nombre": "Street Fighter 6", "plataforma": "PC / PS5 / Xbox", "precio": 59.99, "descripcion": "La nueva evolución de la saga de lucha de Capcom combina modos innovadores y gráficos de última.", "imagen": "12"},
            {"nombre": "The Legend of Zelda: Tears of the Kingdom", "plataforma": "Nintendo Switch", "precio": 69.99, "descripcion": "Una aventura épica a través de los cielos y las tierras de Hyrule en la secuela del éxito de Nintendo.", "imagen": "17"},
            {"nombre": "Super Mario Bros. Wonder", "plataforma": "Nintendo Switch", "precio": 59.99, "descripcion": "La clásica jugabilidad de Mario da un vuelco con la llegada de las divertidísimas Flores Maravilla.", "imagen": "6"}
        ]

        for item in juegos_data:
            # Si existen duplicados previos por nombre, limpiamos el exceso primero
            repetidos = Juego.objects.filter(nombre=item["nombre"])
            if repetidos.count() > 1:
                # Nos quedamos con el primero y borramos los duplicados sobrantes
                primer_juego = repetidos.first()
                repetidos.exclude(pk=primer_juego.pk).delete()

            # Usamos update_or_create buscando por nombre de forma segura
            Juego.objects.update_or_create(
                nombre=item["nombre"],
                defaults={
                    "plataforma": item["plataforma"],
                    "precio": item["precio"],
                    "descripcion": item["descripcion"],
                    "imagen": item["imagen"]
                }
            )

        self.stdout.write(self.style.SUCCESS('¡Los 18 juegos oficiales se cargaron con éxito sin duplicados!'))