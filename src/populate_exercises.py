from exercise.models import ExerciseList

exercise_types = [
    "Running",
    "Cycling",
    "Swimming",
    "Weightlifting",
    "Yoga",
    "Pilates",
    "Hiking",
    "Rowing",
    "Jumping Rope",
    "Boxing",
    "Martial Arts",
    "Dancing",
    "Walking",
    "Sprinting",
    "Circuit Training",
    "Calisthenics",
    "Kickboxing",
    "Tai Chi",
    "Zumba",
    "CrossFit",
    "Rock Climbing",
    "Surfing",
    "Gymnastics",
    "Barre",
    "TRX",
    "Parkour",
    "Spinning",
    "Powerlifting",
    "Functional Training",
    "Kickboxing",
]

def run() : 
    for exercise_type in exercise_types:
        ExerciseList.objects.create(exercise_type=exercise_type)

    print("Exercise types inserted successfully!")

run()