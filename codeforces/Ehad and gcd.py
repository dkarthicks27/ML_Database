from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import streamlit as st


p_engine = create_engine("postgresql://user:password@localhost:5432/practice_db")
p_engine_dataset = create_engine("postgresql://user:password@localhost:5432/datasets_db")
p_engine.execute("CREATE TABLE IF NOT EXISTS records (name text PRIMARY KEY, details text[])")