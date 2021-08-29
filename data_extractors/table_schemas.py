from sqlalchemy import Table, Column, Integer, String, MetaData, Float, Date, Boolean, DateTime, create_engine, \
    ForeignKey

engine = create_engine('mysql+pymysql://root:password@localhost:3306/ipl')
connection = engine.connect()

meta = MetaData()

player_stats = Table("player_stats", meta,
                Column("player_id", Integer, default=0, primary_key=True),
                Column("tournament_id", Integer, ForeignKey("tournaments.tournament_id"), default=0, primary_key=True),
                Column("full_name", String(40), default=""),
                Column("short_name", String(40), default=""),
                Column("nationality", String(40), default=""),
                Column("date_of_birth", Date),
                Column("right_armed_bowl", Boolean),
                Column("right_handed_bat", Boolean),
                Column("bowling_style", String(40), default=""),
                Column("batting_50s", Integer, default=0),
                Column("batting_100s", Integer, default=0),
                Column("batting_innings", Integer, default=0),
                Column("batting_matches", Integer, default=0),
                Column("batting_runs", Integer, default=0),
                Column("batting_balls", Integer, default=0),
                Column("batting_4s", Integer, default=0),
                Column("batting_6s", Integer, default=0),
                Column("batting_notouts", Integer, default=0),
                Column("batting_high_score", String(40), default=""),
                Column("batting_strike_rate", Float, default=0.0),
                Column("batting_average", Float, default=0.0),
                Column("bowling_bbiw", Integer, default=0),
                Column("bowling_bbir", Integer, default=0),
                Column("bowling_bbmw", Integer, default=0),
                Column("bowling_bbmr", Integer, default=0),
                Column("bowling_4w", Integer, default=0),
                Column("bowling_5w", Integer, default=0),
                Column("bowling_10w", Integer, default=0),
                Column("bowling_innings", Integer, default=0),
                Column("bowling_matches", Integer, default=0),
                Column("bowling_balls", Integer, default=0),
                Column("bowling_runs", Integer, default=0),
                Column("bowling_wide_balls", Integer, default=0),
                Column("bowling_no_balls", Integer, default=0),
                Column("bowling_dots", Integer, default=0),
                Column("bowling_wickets", Integer, default=0),
                Column("bowling_4s", Integer, default=0),
                Column("bowling_6s", Integer, default=0),
                Column("bowling_maidens", Integer, default=0),
                Column("bowling_wmaidens", Integer, default=0),
                Column("bowling_hat_tricks", Integer, default=0),
                Column("bowling_average", Float, default=0.0),
                Column("bowling_economy", Float, default=0.0),
                Column("bowling_sr", Float, default=0.0),
                Column("bowling_overs", Float, default=0.0),
                Column("fielding_catches", Integer, default=0),
                Column("fielding_runouts", Integer, default=0),
                Column("fielding_stumpings", Integer, default=0),
                Column("fielding_innings", Integer, default=0),
                Column("fielding_matches", Integer, default=0)
                )

players = Table("players", meta,
                Column("player_id", Integer, default=0, primary_key=True),
                Column("full_name", String(40), default=""),
                Column("short_name", String(40), default=""),
                Column("nationality", String(40), default=""),
                Column("date_of_birth", Date),
                Column("right_armed_bowl", Boolean),
                Column("right_handed_bat", Boolean),
                Column("bowling_style", String(40), default=""),
                )

tournaments = Table("tournaments", meta,
                    Column("tournament_id", Integer, primary_key=True),
                    Column("name", String(40), default=""),
                    Column("type", String(40), default=""),
                    Column("description", String(40), default=""),
                    Column("provisional", Boolean),
                    Column("start_date", DateTime),
                    Column("end_date", DateTime),
                    Column("number_of_matches", Integer),
                    )

teams = Table("teams", meta,
              Column("team_id", String(40), primary_key=True),
              Column("full_name", String(40), default=""),
              Column("short_name", String(40), default=""),
              Column("abbreviation", String(40), default=""),
              Column("type", String(40), default="")
              )

venues = Table("venues", meta,
              Column("venue_id", String(40), primary_key=True),
              Column("full_name", String(40), default=""),
              Column("short_name", String(40), default=""),
              Column("city", String(40), default=""),
              Column("country", String(40), default="")
              )
