import datetime

from typing import Annotated
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base, str_256


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]


class DateOrm(Base):
    __tablename__ = 'Date'

    id: Mapped[intpk]
    date: Mapped[datetime.date]
    created_at: Mapped[created_at]


class ExchangeOrm(Base):
    __tablename__ = 'Exchange'

    id: Mapped[intpk]
    date: Mapped[int] = mapped_column(ForeignKey('Date.id', ondelete='CASCADE'))
    name: Mapped[str_256]
    location: Mapped[str_256]


class InstrumentOrm(Base):
    __tablename__ = 'Instrument'

    id: Mapped[intpk]
    exchange: Mapped[int] = mapped_column(ForeignKey('Exchange.id', ondelete='CASCADE'))
    name: Mapped[str_256]
    storage_type: Mapped[str_256]
    levels: Mapped[str_256]
    iid: Mapped[int]
    available_interval_begin: Mapped[datetime.time]
    available_interval_end: Mapped[datetime.time]
