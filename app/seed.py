from app.database import SessionLocal, engine, Base
from app.models import Character, Actor

# Create tables
Base.metadata.create_all(bind=engine)

# Start session
db = SessionLocal()

# -------------------------
# RESET DATABASE
# -------------------------

db.query(Character).delete()
db.query(Actor).delete()


# -------------------------
# ACTORS
# -------------------------

actors = [

    Actor(
        name="Amybeth McNulty",
        nationality="Irish-Canadian",
        bio="An actress best known for portraying Anne Shirley in Anne with an E, recognized for her emotional and energetic performance."
    ),

    Actor(
        name="Lucas Jade Zumann",
        nationality="American",
        bio="An actor known for playing Gilbert Blythe in Anne with an E and for roles in film and television."
    ),

    Actor(
        name="Geraldine James",
        nationality="British",
        bio="A veteran actress known for portraying Marilla Cuthbert and for decades of acclaimed stage and screen work."
    ),

    Actor(
        name="R.H. Thomson",
        nationality="Canadian",
        bio="A Canadian actor and playwright known for playing Matthew Cuthbert and for major contributions to theater and television."
    ),

    Actor(
        name="Dalila Bela",
        nationality="Canadian",
        bio="An actress known for portraying Diana Barry, Anne's closest friend, as well as other family and fantasy productions."
    ),

    Actor(
        name="Aymeric Jett Montaz",
        nationality="Canadian",
        bio="An actor known for playing Jerry Baynard and for work in youth-oriented television productions."
    ),

    Actor(
        name="Corrine Koslo",
        nationality="Canadian",
        bio="A respected Canadian actress known for portraying Rachel Lynde and for extensive stage, film, and television work."
    )

]

db.add_all(actors)
db.commit()


# -------------------------
# CHARACTERS
# -------------------------

characters = [

    Character(
        name="Anne Shirley",
        description="An imaginative, intelligent orphan whose curiosity and spirit transform the lives of everyone in Avonlea.",
        actor_id=1
    ),

    Character(
        name="Gilbert Blythe",
        description="A hardworking and compassionate student who develops a deep bond with Anne.",
        actor_id=2
    ),

    Character(
        name="Marilla Cuthbert",
        description="A strict but caring guardian who adopts Anne and gradually grows deeply attached to her.",
        actor_id=3
    ),

    Character(
        name="Matthew Cuthbert",
        description="A shy and gentle farmer who quickly becomes Anne's strongest emotional supporter.",
        actor_id=4
    ),

    Character(
        name="Diana Barry",
        description="Anne's loyal best friend who shares in her adventures, dreams, and mischief.",
        actor_id=5
    ),

    Character(
        name="Jerry Baynard",
        description="A farmhand and Anne's friend who teaches her practical skills and French phrases.",
        actor_id=6
    ),

    Character(
        name="Rachel Lynde",
        description="An outspoken village neighbor known for her strong opinions and hidden kindness.",
        actor_id=7
    )

]

db.add_all(characters)
db.commit()


print("Database seeded successfully.")