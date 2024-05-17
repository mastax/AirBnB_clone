#!/usr/bin/python3
"""Module That Executes Each Time That Models Package Is Imported"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()