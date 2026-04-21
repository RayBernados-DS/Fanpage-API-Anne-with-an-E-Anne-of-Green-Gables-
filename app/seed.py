from app.database import SessionLocal, engine, Base
from app.models import Character, Actor

Base.metadata.create_all(bind=engine)


def seed_data():
    db = SessionLocal()

    # reset tables
    db.query(Character).delete()
    db.query(Actor).delete()

    # ---------------- ACTORS ----------------
    actors = [
        Actor(
            name="Amybeth McNulty",
            nationality="Irish-Canadian",
            bio="Known for playing Anne Shirley in Anne with an E."
        ),
        Actor(
            name="Lucas Jade Zumann",
            nationality="American",
            bio="Known for playing Gilbert Blythe in Anne with an E."
        ),
        Actor(
            name="Geraldine James",
            nationality="British",
            bio="Veteran actress who played Marilla Cuthbert."
        ),
        Actor(
            name="R.H. Thomson",
            nationality="Canadian",
            bio="Actor who portrayed Matthew Cuthbert."
        ),
        Actor(
            name="Dalila Bela",
            nationality="Canadian",
            bio="Actress who played Diana Barry."
        ),
        Actor(
            name="Aymeric Jett Montaz",
            nationality="Canadian",
            bio="Actor who played Jerry Baynard."
        ),
        Actor(
            name="Corrine Koslo",
            nationality="Canadian",
            bio="Actress who played Rachel Lynde."
        )
    ]

    db.add_all(actors)
    db.commit()

    # ---------------- CHARACTERS ----------------
    characters = [
        Character(
            name="Anne Shirley",
            description="Imaginative orphan whose presence transforms Avonlea.",
            actor_id=1
        ),
        Character(
            name="Gilbert Blythe",
            description="Anne's academic rival and close companion.",
            actor_id=2
        ),
        Character(
            name="Marilla Cuthbert",
            description="Strict guardian who grows to love Anne deeply.",
            actor_id=3
        ),
        Character(
            name="Matthew Cuthbert",
            description="Kind farmer who immediately bonds with Anne.",
            actor_id=4
        ),
        Character(
            name="Diana Barry",
            description="Anne's loyal best friend.",
            actor_id=5
        ),
        Character(
            name="Jerry Baynard",
            description="Farmhand and friend of Anne.",
            actor_id=6
        ),
        Character(
            name="Rachel Lynde",
            description="Opinionated neighbor of Avonlea.",
            actor_id=7
        )
    ]

    db.add_all(characters)
    db.commit()
    db.close()