# connect.py
from neo4j import GraphDatabase
import config


def get_neo4j_driver():
    return GraphDatabase.driver(config.NEO4J_URI, auth=(config.NEO4J_USERNAME, config.NEO4J_PASSWORD))
