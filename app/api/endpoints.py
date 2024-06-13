from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.config import ConfigCreate, ConfigUpdate, ConfigOut
from app.crud.config import create_config, get_config_by_country, update_config, delete_config
from app.db.session import get_db

router = APIRouter()

@router.post("/create_configuration", response_model=ConfigOut)
def create_configuration(config: ConfigCreate, db: Session = Depends(get_db)):
    """
    Create a new configuration for a country.

    Args:
        config (ConfigCreate): The configuration details for a country.
        db (Session): Database session.

    Returns:
        ConfigOut: The created configuration.
    """
    db_config = get_config_by_country(db, country_code=config.country_code)
    if db_config:
        raise HTTPException(status_code=400, detail="Configuration already exists for this country")
    return create_config(db=db, config=config)

@router.get("/get_configuration/{country_code}", response_model=ConfigOut)
def read_configuration(country_code: str, db: Session = Depends(get_db)):
    """
    Get the configuration details for a country.

    Args:
        country_code (str): The country code.
        db (Session): Database session.

    Returns:
        ConfigOut: The configuration details.
    """
    db_config = get_config_by_country(db, country_code=country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config

@router.post("/update_configuration", response_model=ConfigOut)
def update_configuration(config: ConfigUpdate, db: Session = Depends(get_db)):
    """
    Update the configuration details for a country.

    Args:
        config (ConfigUpdate): The updated configuration details.
        db (Session): Database session.

    Returns:
        ConfigOut: The updated configuration.
    """
    db_config = get_config_by_country(db, country_code=config.country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return update_config(db=db, config=config)

@router.delete("/delete_configuration/{country_code}")
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    """
    Delete the configuration for a country.

    Args:
        country_code (str): The country code.
        db (Session): Database session.

    Returns:
        dict: A message indicating the deletion status.
    """
    db_config = get_config_by_country(db, country_code=country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    delete_config(db=db, country_code=country_code)
    return {"message": "Configuration deleted"}
