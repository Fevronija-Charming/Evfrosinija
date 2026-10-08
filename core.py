import flet as flet
import asyncio
#ШИФРОВАНИЕ ПАРОЛЕЙ
import bcrypt
import time
import datetime
import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
from faststream.rabbit import RabbitBroker
broker=RabbitBroker(url=os.getenv("CLOUDAMQP_URL"))
import redis
redis_client=redis.Redis.from_url(os.getenv("REDIS_URL"),decode_responses=True)
#работа с базой данных
from sqlalchemy import  DateTime, String, Float, Column, Integer, func,Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
engine = create_async_engine(url=os.getenv("DBURL"),echo=True,max_overflow=5)
session_factory = async_sessionmaker(bind=engine,class_=AsyncSession,expire_on_commit=False,autoflush=True)
from pydantic import BaseModel, Field, ValidationError
from sqlalchemy import DateTime, String, Float, Column, Integer, func, Text, BIGINT
from sqlalchemy import  select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
class Base(DeclarativeBase):
    pass
class Users(Base):
    __tablename__="Пользователи"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    Никнейм: Mapped[str] = mapped_column(String(32), nullable=False)
    ОтпечатокПароля: Mapped[str] = mapped_column(String(64), nullable=False)
    Должность: Mapped[str] = mapped_column(String(32), nullable=False)
    Разрешение: Mapped[str] = mapped_column(String(32), nullable=False)
class Platoky(Base):
    __tablename__="ПППЛАТКИ"
    id: Mapped[int]=mapped_column(primary_key=True, autoincrement=True, nullable=False)
    Название: Mapped[str]=mapped_column(String(128), nullable=False)
    Автор: Mapped[str]=mapped_column(String(128), nullable=False)
    Колорит_1: Mapped[str]=mapped_column(String(128), nullable=False)
    Колорит_2: Mapped[str] = mapped_column(String(128), nullable=False)
    Колорит_3: Mapped[str] = mapped_column(String(128), nullable=False)
    Колорит_4: Mapped[str] = mapped_column(String(128), nullable=False)
    Колорит_5: Mapped[str] = mapped_column(String(128), nullable=False)
    Узор_темени: Mapped[str] = mapped_column(String(128), nullable=False)
    Узор_сердцевины: Mapped[str] = mapped_column(String(128), nullable=False)
    Узор_сторон: Mapped[str] = mapped_column(String(128), nullable=False)
    Узор_углов: Mapped[str] = mapped_column(String(128), nullable=False)
    Узор_края: Mapped[str] = mapped_column(String(128), nullable=False)
    Цветы_Орнамент: Mapped[str] = mapped_column(String(128), nullable=False)
    Изображенный_Цветок_1: Mapped[str] = mapped_column(String(128), nullable=False)
    Изображенный_Цветок_2: Mapped[str] = mapped_column(String(128), nullable=False)
    Изображенный_Цветок_3: Mapped[str] = mapped_column(String(128), nullable=False)
    Изображенный_Цветок_4: Mapped[str] = mapped_column(String(128), nullable=False)
    Изображенный_Цветок_5: Mapped[str] = mapped_column(String(128), nullable=False)
    Размер_Платка: Mapped[str]=mapped_column(String(128), nullable=False)
    Материал_Платка: Mapped[str]=mapped_column(String(128), nullable=False)
    Материал_Бахромы: Mapped[str]=mapped_column(String(128), nullable=False)
class Platok_Schema(BaseModel):
    id: int
    Название_Платка: str = Field(min_length=5, max_length=50)
    Автор_Платка: str = Field(min_length=5, max_length=50)
    Колорит_1: str= Field(min_length=3, max_length=50)
    Колорит_2: str= Field(min_length=3, max_length=50)
    Колорит_3: str= Field(min_length=3, max_length=50)
    Колорит_4: str= Field(min_length=3, max_length=50)
    Колорит_5: str= Field(min_length=3, max_length=50)
    Узор_Темени: str= Field(min_length=3, max_length=50)
    Узор_Сердцевины: str= Field(min_length=3, max_length=50)
    Узор_Сторон: str= Field(min_length=3, max_length=50)
    Узор_Углов: str= Field(min_length=3, max_length=50)
    Узор_Края: str= Field(min_length=3, max_length=50)
    Цветы_Орнамент: str= Field(min_length=3, max_length=50)
    Изображённый_Цветок_1: str= Field(min_length=3, max_length=50)
    Изображённый_Цветок_2: str= Field(min_length=3, max_length=50)
    Изображённый_Цветок_3: str= Field(min_length=3, max_length=50)
    Изображённый_Цветок_4: str= Field(min_length=3, max_length=50)
    Изображённый_Цветок_5: str= Field(min_length=3, max_length=50)
    Размер_Платка: str= Field(min_length=3, max_length=50)
    Материал_Платка: str= Field(min_length=3, max_length=50)
    Материал_Бахромы: str= Field(min_length=3, max_length=50)
class Publikacii(Base):
    __tablename__ = "Публикации"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    Дата_время_публикации: Mapped[str] = mapped_column(String(16), nullable=False)
    Текст_публикации: Mapped[str] = mapped_column(Text, nullable=False)
    Ссылка_фото_публикации_1: Mapped[str] = mapped_column(String(100), nullable=False)
    Ссылка_фото_публикации_2: Mapped[str] = mapped_column(String(100), nullable=False)
    Ссылка_фото_публикации_3: Mapped[str] = mapped_column(String(100), nullable=False)
    Ссылка_фото_публикации_4: Mapped[str] = mapped_column(String(100), nullable=False)
    Ссылка_фото_публикации_5: Mapped[str] = mapped_column(String(100), nullable=False)
    Ссылка_на_сайт_с_материалом: Mapped[str] = mapped_column(String(100), nullable=False)
    Ссылка_на_документ_с_материалом: Mapped[str] = mapped_column(String(100), nullable=False)
class Publikacii_Schema(BaseModel):
    Дата_Время_Публикации: str = Field(min_length=15, max_length=16)
    Текст_публикации: str = Field(min_length=16, max_length=3000)
    Ссылка_фото_публикации_1: str = Field(min_length=83, max_length=85)
    Ссылка_фото_публикации_2: str = Field(min_length=83, max_length=85)
    Ссылка_фото_публикации_3: str = Field(min_length=83, max_length=85)
    Ссылка_фото_публикации_4: str = Field(min_length=83, max_length=85)
    Ссылка_фото_публикации_5: str = Field(min_length=83, max_length=85)
    Ссылка_на_сайт_с_материалом: str = Field(min_length=10, max_length=100)
    Ссылка_на_документ_с_материалом: str = Field(min_length=70, max_length=72)
class Polzovatel_Schema(BaseModel):
    Имя_Пользователя: str = Field(min_length=4, max_length=16)
    Пароль: str = Field(min_length=4, max_length=32)
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
cvet_2=flet.Colors.AMBER_ACCENT
cvet_1=flet.Colors.DEEP_ORANGE
razmer_bukov=24
async def register_auth_fail():
    intsident_time=str(datetime.datetime.now())
    intsident_value="Evfrosinija:auth-fail:"+str(time.time())
    redis_client.set(intsident_value, intsident_time,ex=300)
async def opovestitel_publikacii(message_plain:str):
    async with broker:
        await broker.publish(message="ЕФРОСИНИЯ СООБЩАЕТ, ДОБАВЛЕНА ПУБЛИКАЦИЯ", queue="PLATOKY")
        await broker.publish(message=message_plain, queue="PLATOKY")
async def opovestitel(message_plain:str):
    async with broker:
        await broker.publish(message="ЕФРОСИНИЯ СООБЩАЕТ, ДОБАВЛЕН ПЛАТОК", queue="PLATOKY")
        await broker.publish(message=message_plain, queue="PLATOKY")
async def vvod_publikacii(publikacija_flet_data:dict):
    session = session_factory()

    async with session:
        sost_vvoda_publikacii=0
        try:
            publikacija_zapis = Publikacii(Дата_время_публикации=publikacija_flet_data.get("Дата_Время_Публикации",None),
                                       Ссылка_фото_публикации_1=publikacija_flet_data.get("Ссылка_фото_публикации_1",None),
                                       Ссылка_фото_публикации_2=publikacija_flet_data.get("Ссылка_фото_публикации_2",None),
                                       Ссылка_фото_публикации_3=publikacija_flet_data.get("Ссылка_фото_публикации_3",None),
                                       Ссылка_фото_публикации_4=publikacija_flet_data.get("Ссылка_фото_публикации_4",None),
                                       Ссылка_фото_публикации_5=publikacija_flet_data.get("Ссылка_фото_публикации_5",None),
                                       Ссылка_на_сайт_с_материалом=publikacija_flet_data.get("Ссылка_на_сайт_с_материалом",None),
                                       Ссылка_на_документ_с_материалом=publikacija_flet_data.get("Ссылка_на_документ_с_материалом",None),
                                       Текст_публикации=publikacija_flet_data.get("Текст_публикации",None),)
            session.add(publikacija_zapis)
            await session.commit()
            await session.close()
            sost_vvoda_publikacii = 0
            return sost_vvoda_publikacii
        except:
            await session.rollback()
            await session.close()
            sost_vvoda_publikacii=1
            return sost_vvoda_publikacii
async def vvod_platka(platok_s_flet_data:dict):
    try:
        artikul = platok_s_flet_data.get("id", None)
        query1 = select(Platoky).where(Platoky.id == int(artikul))
        session = session_factory()
        result1 = await session.execute(query1)
        artikul_DB = result1.scalars().first()
        if artikul_DB is None:
            nazvanije = platok_s_flet_data.get("Название_Платка", None)
            query2 = select(Platoky).where(Platoky.Название == nazvanije)
            result2 = await session.execute(query2)
            nazvanije_DB = result2.scalars().first()
            if nazvanije_DB is None:
                platoch_eksemp = Platoky(id=int(platok_s_flet_data.get("id", None)),
                Название=platok_s_flet_data.get("Название_Платка",None),
                Автор=platok_s_flet_data.get("Автор_Платка",None),
                Колорит_1=platok_s_flet_data.get("Колорит_1",None),
                Колорит_2=platok_s_flet_data.get("Колорит_2", None),
                Колорит_3=platok_s_flet_data.get("Колорит_3", None),
                Колорит_4=platok_s_flet_data.get("Колорит_4", None),
                Колорит_5=platok_s_flet_data.get("Колорит_5", None),
                Узор_темени=platok_s_flet_data.get("Узор_Темени", None),
                Узор_сердцевины=platok_s_flet_data.get("Узор_Сердцевины",None),
                Узор_сторон=platok_s_flet_data.get("Узор_Сторон",None),
                Узор_углов=platok_s_flet_data.get("Узор_Углов",None),
                Узор_края=platok_s_flet_data.get("Узор_Края",None),
                Цветы_Орнамент=platok_s_flet_data.get("Цветы_Орнамент",None),
                Изображенный_Цветок_1=platok_s_flet_data.get("Изображённый_Цветок_1",None),
                Изображенный_Цветок_2=platok_s_flet_data.get("Изображённый_Цветок_2",None),
                Изображенный_Цветок_3=platok_s_flet_data.get("Изображённый_Цветок_3",None),
                Изображенный_Цветок_4=platok_s_flet_data.get("Изображённый_Цветок_4",None),
                Изображенный_Цветок_5=platok_s_flet_data.get("Изображённый_Цветок_5",None),
                Размер_Платка=platok_s_flet_data.get("Размер_Платка",None),
                Материал_Платка=platok_s_flet_data.get("Материал_Платка",None),
                Материал_Бахромы=platok_s_flet_data.get("Материал_Бахромы",None))
                session.add(platoch_eksemp)
                await session.commit()
                await session.close()
                vvod_sost=3
                return vvod_sost
            else:
                vvod_sost=2
                await session.close()
                return vvod_sost
        else:
            vvod_sost=1
            await session.close()
            return vvod_sost
    except:
        vvod_sost=0
        return vvod_sost
async def create_platoky():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
async def vstavka_polzovateley():
    session = session_factory()
    async with session:
        polzovatel_ekmsemp=Users(id=1,Никнейм='Fevronija',ОтпечатокПароля='$2b$12$lwVrIRESZQFNTEFO2Ad0ZenuGx.gbaDfAjYmNPuLCSW.g.KKJRO0W',
                                 Должность='Директор',Разрешение='Активен')
        session.add(polzovatel_ekmsemp)
        polzovatel_ekmsemp_2=Users(id=2,Никнейм='Sekleteja',ОтпечатокПароля='$2b$12$AqukeKiOKxqwmuBc8vBTSuBbYzSSi4aa8EzwTeyGnHVpmjVLEOUM2',
                                 Должность='Техник',Разрешение='Активен')
        session.add(polzovatel_ekmsemp_2)
        polzovatel_ekmsemp_3=Users(id=3,Никнейм='Epistima',ОтпечатокПароля='$2b$12$Ri9kVo0.XjfDU/PDWoucQunMZxHGDjNDW3JNyFOZXvoQcz3satQT2',
                                 Должность='Копирайтер',Разрешение='Активен')
        session.add(polzovatel_ekmsemp_3)
        await session.commit()
        await session.close()
async def proverka_blokirovka():
    prefix="Evfrosinija:auth-fail:*"
    blokirovka_raboty = 0
    auth_fail_count= 0
    for key in redis_client.scan_iter(prefix):
        auth_fail_count=auth_fail_count+1
    if auth_fail_count>5:
        blokirovka_raboty=1
    return blokirovka_raboty
async def main(page:flet.Page):
    # await create_platoky()
    # await vstavka_polzovateley()
    # redis_client.flushall()
    page.fonts = {"Ponomar": "Fedorovsk-Regular.ttf"}
    page.width = 600
    page.height = 1000
    page.theme = flet.Theme(font_family="Ponomar")
    page.title = "Добавить платок"
    page.theme_mode = flet.ThemeMode.LIGHT
    page.resizable = False
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    def pustyshka(e):
        print(e)
        page.update()
    image_side_4 = flet.Image(src=f"carica-tenban.jpg", width=590, height=875)
    image_side_5= flet.Image(src=f"carica-tenban.jpg", width=590, height=875)
    knopka_oshibka_popytok = flet.FilledButton("ПРЕВЫШЕННО КОЛИЧЕСТВО ПОПЫТОК ВХОДА", width=375, height=60,
                                               on_click=pustyshka,
                                               disabled=False, visible=True,
                                               style=flet.ButtonStyle(color=flet.Colors.RED,
                                                                      bgcolor=flet.Colors.PURPLE))

    form_container_20 = flet.Container(width=280, height=400, top=400, left=20,
                                       content=flet.Column([knopka_oshibka_popytok], ))
    content_pirog_5 = flet.Stack([image_side_4, form_container_20])
    blokirovka_raboty= await proverka_blokirovka()
    if blokirovka_raboty==1:
        page.add(flet.Column([content_pirog_5],))
        snack = page.snack_bar = flet.SnackBar(
            content=flet.Text("ПРЕВЫШЕНО ЧИСЛО ПОПЫТОК ВХОДА", color=flet.Colors.PURPLE_ACCENT, size=28,
                              weight=flet.FontWeight.W_100,
                              font_family="Ponomar"), bgcolor=flet.Colors.RED)
        page.show_dialog(snack)
        page.update()
    else:
        async def na_glavnuju(e):
            await flet.UrlLauncher().launch_url("www.platoki.ee")
        async def panel_vhoda(e):
            page.clean()
            page.add(content_pirog_4)
        async def posle_vyhoda(e):
            page.clean()
            page.add(content_pirog_9)
            snack = page.snack_bar = flet.SnackBar(
                content=flet.Text("СПАСИБО ЗА РАБОТУ! АНГЕЛА-ХРАНИТЕЛЯ", color=flet.Colors.BLUE_GREY, size=28,
                                  weight=flet.FontWeight.W_100,
                                  font_family="Ponomar"), bgcolor=flet.Colors.BLUE)
            page.show_dialog(snack)
            page.update()
        async def oshibka_vhoda():
            knopka_oshibki_vhoda.visible=True
            knopka_vhod.disabled=True
            snack = page.snack_bar = flet.SnackBar(
                content=flet.Text("ОШИБКА ВХОДА ВВЕДЕНЫ НЕКОРРЕКТНЫЕ ДАННЫЕ", color=flet.Colors.PURPLE_ACCENT, size=28,
                              weight=flet.FontWeight.W_100,
                              font_family="Ponomar"), bgcolor=flet.Colors.RED)
            page.show_dialog(snack)
            page.update()
        async def validate_user(e):
            blokirovka_raboty=await proverka_blokirovka()
            if blokirovka_raboty==1:
                page.clean()
                page.add(flet.Column([content_pirog_5],))
                snack = page.snack_bar = flet.SnackBar(
                content=flet.Text("ПРЕВЫШЕННО КОЛИЧЕСТВО ПОПЫТОК ВХОДА", color=flet.Colors.PURPLE_ACCENT, size=28,
                                  weight=flet.FontWeight.W_100,
                                  font_family="Ponomar"), bgcolor=flet.Colors.RED)
                page.show_dialog(snack)
                page.update()
            else:
                session = session_factory()
                async with session:
                    inserted_username=imja_polzovatelja.value
                    query0 = select(Users).where(Users.Никнейм == inserted_username)
                    result0 = await session.execute(query0)
                    polzovatel_DB = result0.scalars().first()
                    if polzovatel_DB is None:
                        await oshibka_vhoda()
                        await register_auth_fail()
                    else:
                        query00 = select(Users.ОтпечатокПароля).where(Users.Никнейм == inserted_username)
                        result00 = await session.execute(query00)
                        password_DB = result00.scalars().all()[0]
                        hash_etal=password_DB.encode("utf-8")
                        inserted_password=parol_polzovatelja.value
                        password_bytes=inserted_password.encode("utf-8")
                        is_correct=bcrypt.checkpw(password_bytes,hash_etal)
                        if is_correct:
                            query000=select(Users.Разрешение).where(Users.Никнейм == inserted_username)
                            result000 = await session.execute(query000)
                            user_status = result000.scalars().all()[0]
                            if user_status == "Активен":
                                query0000 = select(Users.Должность).where(Users.Никнейм == inserted_username)
                                result0000 = await session.execute(query0000)
                                user_role = result0000.scalars().all()[0]
                                if user_role == "Директор":
                                    page.clean()
                                    page.add(flet.Column([content_pirog_2],))
                                    await session.close()
                                elif user_role == "Техник":
                                    page.clean()
                                    page.add(flet.Column([content_tehnik],))
                                    await session.close()
                                elif user_role == "Копирайтер":
                                    page.clean()
                                    page.add(flet.Column([content_market], ))
                                    await session.close()
                                elif user_role == "Продавец":
                                    page.clean()
                                    page.add(flet.Column([content_prodavec], ))
                                    page.update()
                                    await session.close()
                            else:
                                page.clean()
                                page.add(flet.Column([content_pirog_6], ))
                                await session.close()
                        else:
                            await oshibka_vhoda()
                            await register_auth_fail()
                            await session.close()
        async def glavnaja_otrisovka(e):
            page.clean()
            page.add(flet.Column([  # image_side,
            # data_table,
            # form_side
            content_pirog_2],
            # scroll=flet.ScrollMode.AUTO
            ))
            page.overlay.clear()
            page.update()
        async def panelvhoda_otrisovka(e):
            page.clean()
            page.add(flet.Column([  # image_side,
            # data_table,
            # form_side
            content_pirog_4],
            # scroll=flet.ScrollMode.AUTO
            ))
            page.overlay.clear()
            page.update()
        knopka_tenban_1 = flet.FilledButton("ВАША УЧЁТНАЯ ЗАПИСЬ ЗАБЛОКИРОВАНА", width=350, height=60,
                                            on_click=pustyshka,
                                            disabled=True, visible=True,
                                            style=flet.ButtonStyle(color=flet.Colors.BLUE_50,
                                                                   bgcolor=flet.Colors.BLUE))
        knopka_tenban_2 = flet.FilledButton("ДОСТУП К РЕСУРСУ ОГРАНИЧЕН", width=350, height=60,
                                            on_click=pustyshka,
                                            disabled=False, visible=True,
                                            style=flet.ButtonStyle(color=flet.Colors.BLUE_50,
                                                                   bgcolor=flet.Colors.BLUE))
        knopka_tenban_3 = flet.FilledButton("ДЛЯ РАЗБЛОКИРОВКИ СВЯЖИТЕСЬ С АДМИНИСТРАТОРОМ", width=350, height=60,
                                            on_click=pustyshka,
                                            disabled=False, visible=True,
                                            style=flet.ButtonStyle(color=flet.Colors.BLUE_50,
                                                                   bgcolor=flet.Colors.BLUE))
        #knopka_tenban_4 = flet.FilledButton("НАЗАД НА ГЛАВНУЮ", width=350, height=60, on_click=panelvhoda_otrisovka,
                                                #disabled=False, visible=True,
                                                #style=flet.ButtonStyle(color=cvet_1, bgcolor=cvet_2))
        form_container_21 = flet.Container(width=280, height=400, top=350, left=10,
                                           content=flet.Column([knopka_tenban_1], ))
        form_container_22 = flet.Container(width=280, height=400, top=450, left=10,
                                           content=flet.Column([knopka_tenban_2], ))
        form_container_23 = flet.Container(width=280, height=400, top=550, left=10,
                                           content=flet.Column([knopka_tenban_3], ))
        #form_container_24 = flet.Container(width=280, height=400, top=600, left=10,
                                           #content=flet.Column([knopka_tenban_4], ))
        content_pirog_6 = flet.Stack([image_side_5, form_container_21,form_container_22,form_container_23,#form_container_24
                                      ])
        async def platok_otrisovka(e):
            page.clean()
            page.add(flet.Column([  # image_side,
            # data_table,
            # form_side
            content_pirog],
            # scroll=flet.ScrollMode.AUTO
            ))
        async def publikacija_otrisovka(e):
            page.clean()
            page.add(flet.Column([  # image_side,
            # data_table,
            # form_side
            content_pirog_3],
            # scroll=flet.ScrollMode.AUTO
            ))
            page.update()
        async def prodavec_menju_otrisovka(e):
            page.clean()
            page.add(flet.Column([content_prodavec],
            # scroll=flet.ScrollMode.AUTO
            ))
            page.update()
        async def tehnik_menju_otrisovka(e):
            page.clean()
            page.add(flet.Column([content_tehnik],
            # scroll=flet.ScrollMode.AUTO
            ))
            page.update()
        async def market_menju_otrisovka(e):
            page.clean()
            page.add(flet.Column([content_market],
            # scroll=flet.ScrollMode.AUTO
            ))
            page.update()
        #МКНОПКТ
        knopka_bazadannyh_glavnaja = flet.FilledButton("НАЗАД НА ГЛАВНУЮ", width=125, height=40,
                                                       on_click=glavnaja_otrisovka,
                                                       disabled=False, visible=True,
                                                       style=flet.ButtonStyle(color=flet.Colors.BLUE_50,
                                                                              bgcolor=flet.Colors.BLUE))
        knopka_tehnik_na_glavnuju = flet.FilledButton("НАЗАД НА ГЛАВНУЮ", width=125, height=40,
                                                      on_click=tehnik_menju_otrisovka,
                                                      disabled=False, visible=True,
                                                      style=flet.ButtonStyle(color=flet.Colors.BLUE_50,
                                                                             bgcolor=flet.Colors.BLUE))
        knopka_prodavec_na_glavnuju = flet.FilledButton("НАЗАД НА ГЛАВНУЮ", width=125, height=40,
                                                        on_click=prodavec_menju_otrisovka,
                                                        disabled=False, visible=True,
                                                        style=flet.ButtonStyle(color=flet.Colors.BLUE_50,
                                                                               bgcolor=flet.Colors.BLUE))
        knopka_marketolog_na_glavnuju = flet.FilledButton("НАЗАД НА ГЛАВНУЮ", width=125, height=40,
                                                          on_click=market_menju_otrisovka,
                                                          disabled=False, visible=True,
                                                          style=flet.ButtonStyle(color=flet.Colors.BLUE_50,
                                                                                 bgcolor=flet.Colors.BLUE))
        #МСОТРИСОВКА ТАБЛИЦ С БД
        async def knigaotzyv_otrisovka(e):
            page.clean()
            page.add(table_container3)
        async def bazadannyh_otrisovka(e):
            # ТАБЛИЦА ПО ПЛАТКАМ:
            table_colums = [
                flet.DataColumn(flet.Text("Артикул")),
                flet.DataColumn(flet.Text("Название")),
                flet.DataColumn(flet.Text("Автор платка")),
                flet.DataColumn(flet.Text("Колорит 1")),
                flet.DataColumn(flet.Text("Колорит 2")),
                flet.DataColumn(flet.Text("Колорит 3")),
                flet.DataColumn(flet.Text("Колорит 4")),
                flet.DataColumn(flet.Text("Колорит 5")),
                flet.DataColumn(flet.Text("Узор темени")),
                flet.DataColumn(flet.Text("Узор сердцевины")),
                flet.DataColumn(flet.Text("Узор сторон")),
                flet.DataColumn(flet.Text("Узор углов")),
                flet.DataColumn(flet.Text("Узор краёв")),
                flet.DataColumn(flet.Text("Соотношение рисунка и орнамента")),
                flet.DataColumn(flet.Text("Нарисованный цветок 1")),
                flet.DataColumn(flet.Text("Нарисованный цветок 2")),
                flet.DataColumn(flet.Text("Нарисованный цветок 3")),
                flet.DataColumn(flet.Text("Нарисованный цветок 4")),
                flet.DataColumn(flet.Text("Нарисованный цветок 5")),
                flet.DataColumn(flet.Text("Размер платка")),
                flet.DataColumn(flet.Text("Материал платка")),
                flet.DataColumn(flet.Text("Материал бахромы"))]
            # ЗДЕСЬ СТИЛИЗАЦИЯ ТАБЛИЦЫ ИМЕННО В ФЛЕТЕ
            data_table = flet.DataTable(heading_row_color=flet.Colors.BLUE_100,
                                          border=flet.Border(bottom=flet.BorderSide(2, flet.Colors.BLUE),
                                                             left=flet.BorderSide(2, flet.Colors.BLUE),
                                                             right=flet.BorderSide(2, flet.Colors.BLUE)),
                                          vertical_lines=flet.BorderSide(2, flet.Colors.BLUE),
                                          horizontal_lines=flet.BorderSide(10, flet.Colors.BLUE), columns=table_colums,
                                          rows=[])
            #      НАПОЛНЕНИЕ ТАБЛИЦЫ ДАННЫМИ
            from db_data_perfom import platoky_data
            records=platoky_data()
            for record in records:
                data_table.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text(record[0])),
                                                                 flet.DataCell(flet.Text(record[1])),
                                                                 flet.DataCell(flet.Text(record[2])),
                                                                 flet.DataCell(flet.Text(record[3])),
                                                                 flet.DataCell(flet.Text(record[4])),
                                                                 flet.DataCell(flet.Text(record[5])),
                                                                 flet.DataCell(flet.Text(record[6])),
                                                                 flet.DataCell(flet.Text(record[7])),
                                                                 flet.DataCell(flet.Text(record[8])),
                                                                 flet.DataCell(flet.Text(record[9])),
                                                                 flet.DataCell(flet.Text(record[10])),
                                                                 flet.DataCell(flet.Text(record[11])),
                                                                 flet.DataCell(flet.Text(record[12])),
                                                                 flet.DataCell(flet.Text(record[13])),
                                                                 flet.DataCell(flet.Text(record[14])),
                                                                 flet.DataCell(flet.Text(record[15])),
                                                                 flet.DataCell(flet.Text(record[16])),
                                                                 flet.DataCell(flet.Text(record[17])),
                                                                 flet.DataCell(flet.Text(record[18])),
                                                                 flet.DataCell(flet.Text(record[19])),
                                                                 flet.DataCell(flet.Text(record[20])),
                                                                 flet.DataCell(flet.Text(record[21])), ], ))
            data_table.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text("~")),flet.DataCell(knopka_bazadannyh_glavnaja),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")), ]))
            table_container = flet.Column(controls=[flet.Row(controls=[data_table], scroll=flet.ScrollMode.ALWAYS)],
                                          expand=True, scroll=flet.ScrollMode.ALWAYS)
            page.clean()
            page.add(table_container)
        async def zurnalposech_otrisovka(e):
            page.clean()
            page.add(table_container2)
        async def bazadannyh_Teh_otrisovka(e):
            # ТАБЛИЦА ПО ПЛАТКАМ:
            table_colums = [flet.DataColumn(flet.Text("Артикул")), flet.DataColumn(flet.Text("Название")),
                            flet.DataColumn(flet.Text("Автор платка")), flet.DataColumn(flet.Text("Колорит 1")),
                            flet.DataColumn(flet.Text("Колорит 2")), flet.DataColumn(flet.Text("Колорит 3")),
                            flet.DataColumn(flet.Text("Колорит 4")), flet.DataColumn(flet.Text("Колорит 5")),
                            flet.DataColumn(flet.Text("Узор темени")), flet.DataColumn(flet.Text("Узор сердцевины")),
                            flet.DataColumn(flet.Text("Узор сторон")), flet.DataColumn(flet.Text("Узор углов")),
                            flet.DataColumn(flet.Text("Узор краёв")),
                            flet.DataColumn(flet.Text("Соотношение рисунка и орнамента")),
                            flet.DataColumn(flet.Text("Нарисованный цветок 1")),
                            flet.DataColumn(flet.Text("Нарисованный цветок 2")),
                            flet.DataColumn(flet.Text("Нарисованный цветок 3")),
                            flet.DataColumn(flet.Text("Нарисованный цветок 4")),
                            flet.DataColumn(flet.Text("Нарисованный цветок 5")),
                            flet.DataColumn(flet.Text("Размер платка")),
                            flet.DataColumn(flet.Text("Материал платка")),
                            flet.DataColumn(flet.Text("Материал бахромы"))]
            # ЗДЕСЬ СТИЛИЗАЦИЯ ТАБЛИЦЫ ИМЕННО В ФЛЕТЕ
            data_tableTH = flet.DataTable(heading_row_color=flet.Colors.BLUE_100,
                                          border=flet.Border(bottom=flet.BorderSide(2, flet.Colors.BLUE),
                                                             left=flet.BorderSide(2, flet.Colors.BLUE),
                                                             right=flet.BorderSide(2, flet.Colors.BLUE)),
                                          vertical_lines=flet.BorderSide(2, flet.Colors.BLUE),
                                          horizontal_lines=flet.BorderSide(10, flet.Colors.BLUE), columns=table_colums,
                                          rows=[])
            from db_data_perfom import platoky_data
            records = platoky_data()
            for record in records:
                data_tableTH.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text(record[0])),
                                                             flet.DataCell(flet.Text(record[1])),
                                                             flet.DataCell(flet.Text(record[2])),
                                                             flet.DataCell(flet.Text(record[3])),
                                                             flet.DataCell(flet.Text(record[4])),
                                                             flet.DataCell(flet.Text(record[5])),
                                                             flet.DataCell(flet.Text(record[6])),
                                                             flet.DataCell(flet.Text(record[7])),
                                                             flet.DataCell(flet.Text(record[8])),
                                                             flet.DataCell(flet.Text(record[9])),
                                                             flet.DataCell(flet.Text(record[10])),
                                                             flet.DataCell(flet.Text(record[11])),
                                                             flet.DataCell(flet.Text(record[12])),
                                                             flet.DataCell(flet.Text(record[13])),
                                                             flet.DataCell(flet.Text(record[14])),
                                                             flet.DataCell(flet.Text(record[15])),
                                                             flet.DataCell(flet.Text(record[16])),
                                                             flet.DataCell(flet.Text(record[17])),
                                                             flet.DataCell(flet.Text(record[18])),
                                                             flet.DataCell(flet.Text(record[19])),
                                                             flet.DataCell(flet.Text(record[20])),
                                                             flet.DataCell(flet.Text(record[21])), ], ))
            data_tableTH.rows.append(
                flet.DataRow(cells=[flet.DataCell(flet.Text("~")), flet.DataCell(knopka_tehnik_na_glavnuju),
                                    flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),
                                    flet.DataCell(flet.Text("~")),
                                    flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),
                                    flet.DataCell(flet.Text("~")),
                                    flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),
                                    flet.DataCell(flet.Text("~")),
                                    flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),
                                    flet.DataCell(flet.Text("~")),
                                    flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),
                                    flet.DataCell(flet.Text("~")),
                                    flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),
                                    flet.DataCell(flet.Text("~")),
                                    flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")), ]))
            table_containerTH = flet.Column(controls=[flet.Row(controls=[data_tableTH], scroll=flet.ScrollMode.ALWAYS)],
                                            expand=True, scroll=flet.ScrollMode.ALWAYS)
            page.clean()
            page.add(table_containerTH)
        async def zurnalposech_Teh_otrisovka(e):
            page.clean()
            page.add(table_containerTH2)
        async def knigaotzyv_Teh_otrisovka(e):
            page.clean()
            page.add(table_containerTH3)
        async def bazadannyh_PR_otrisovka(e):
            # ТАБЛИЦА ПО ПЛАТКАМ:
            table_colums = [flet.DataColumn(flet.Text("Артикул")),flet.DataColumn(flet.Text("Название")),
                flet.DataColumn(flet.Text("Автор платка")),flet.DataColumn(flet.Text("Колорит 1")),
                flet.DataColumn(flet.Text("Колорит 2")),flet.DataColumn(flet.Text("Колорит 3")),
                flet.DataColumn(flet.Text("Колорит 4")),flet.DataColumn(flet.Text("Колорит 5")),
                flet.DataColumn(flet.Text("Узор темени")),flet.DataColumn(flet.Text("Узор сердцевины")),
                flet.DataColumn(flet.Text("Узор сторон")),flet.DataColumn(flet.Text("Узор углов")),
                flet.DataColumn(flet.Text("Узор краёв")),flet.DataColumn(flet.Text("Соотношение рисунка и орнамента")),
                flet.DataColumn(flet.Text("Нарисованный цветок 1")),flet.DataColumn(flet.Text("Нарисованный цветок 2")),
                flet.DataColumn(flet.Text("Нарисованный цветок 3")),flet.DataColumn(flet.Text("Нарисованный цветок 4")),
                flet.DataColumn(flet.Text("Нарисованный цветок 5")),flet.DataColumn(flet.Text("Размер платка")),
                flet.DataColumn(flet.Text("Материал платка")),flet.DataColumn(flet.Text("Материал бахромы"))]
            # ЗДЕСЬ СТИЛИЗАЦИЯ ТАБЛИЦЫ ИМЕННО В ФЛЕТЕ
            data_tablePR = flet.DataTable(heading_row_color=flet.Colors.BLUE_100,
                                        border=flet.Border(bottom=flet.BorderSide(2, flet.Colors.BLUE),
                                                           left=flet.BorderSide(2, flet.Colors.BLUE),
                                                           right=flet.BorderSide(2, flet.Colors.BLUE)),
                                        vertical_lines=flet.BorderSide(2, flet.Colors.BLUE),
                                        horizontal_lines=flet.BorderSide(10, flet.Colors.BLUE), columns=table_colums,
                                        rows=[])
            from db_data_perfom import platoky_data
            records=platoky_data()
            for record in records:
                data_tablePR.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text(record[0])),
                                                                 flet.DataCell(flet.Text(record[1])),
                                                                 flet.DataCell(flet.Text(record[2])),
                                                                 flet.DataCell(flet.Text(record[3])),
                                                                 flet.DataCell(flet.Text(record[4])),
                                                                 flet.DataCell(flet.Text(record[5])),
                                                                 flet.DataCell(flet.Text(record[6])),
                                                                 flet.DataCell(flet.Text(record[7])),
                                                                 flet.DataCell(flet.Text(record[8])),
                                                                 flet.DataCell(flet.Text(record[9])),
                                                                 flet.DataCell(flet.Text(record[10])),
                                                                 flet.DataCell(flet.Text(record[11])),
                                                                 flet.DataCell(flet.Text(record[12])),
                                                                 flet.DataCell(flet.Text(record[13])),
                                                                 flet.DataCell(flet.Text(record[14])),
                                                                 flet.DataCell(flet.Text(record[15])),
                                                                 flet.DataCell(flet.Text(record[16])),
                                                                 flet.DataCell(flet.Text(record[17])),
                                                                 flet.DataCell(flet.Text(record[18])),
                                                                 flet.DataCell(flet.Text(record[19])),
                                                                 flet.DataCell(flet.Text(record[20])),
                                                                 flet.DataCell(flet.Text(record[21])), ], ))
            data_tablePR.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text("~")),flet.DataCell(knopka_tehnik_na_glavnuju),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")), ]))
            table_containerPR = flet.Column(controls=[flet.Row(controls=[data_tablePR], scroll=flet.ScrollMode.ALWAYS)],
                                          expand=True, scroll=flet.ScrollMode.ALWAYS)
            page.clean()
            page.add(table_containerPR)
        async def zurnalposech_PR_otrisovka(e):
            page.clean()
            page.add(table_containerPR2)
        async def knigaotzyv_PR_otrisovka(e):
            page.clean()
            page.add(table_containerPR3)
        async def bazadannyh_MK_otrisovka(e):
            # ТАБЛИЦА ПО ПЛАТКАМ:
            table_colums = [flet.DataColumn(flet.Text("Артикул")), flet.DataColumn(flet.Text("Название")),
                            flet.DataColumn(flet.Text("Автор платка")), flet.DataColumn(flet.Text("Колорит 1")),
                            flet.DataColumn(flet.Text("Колорит 2")), flet.DataColumn(flet.Text("Колорит 3")),
                            flet.DataColumn(flet.Text("Колорит 4")), flet.DataColumn(flet.Text("Колорит 5")),
                            flet.DataColumn(flet.Text("Узор темени")), flet.DataColumn(flet.Text("Узор сердцевины")),
                            flet.DataColumn(flet.Text("Узор сторон")), flet.DataColumn(flet.Text("Узор углов")),
                            flet.DataColumn(flet.Text("Узор краёв")),
                            flet.DataColumn(flet.Text("Соотношение рисунка и орнамента")),
                            flet.DataColumn(flet.Text("Нарисованный цветок 1")),
                            flet.DataColumn(flet.Text("Нарисованный цветок 2")),
                            flet.DataColumn(flet.Text("Нарисованный цветок 3")),
                            flet.DataColumn(flet.Text("Нарисованный цветок 4")),
                            flet.DataColumn(flet.Text("Нарисованный цветок 5")),
                            flet.DataColumn(flet.Text("Размер платка")),
                            flet.DataColumn(flet.Text("Материал платка")),
                            flet.DataColumn(flet.Text("Материал бахромы"))]
            # ЗДЕСЬ СТИЛИЗАЦИЯ ТАБЛИЦЫ ИМЕННО В ФЛЕТЕ
            data_tableMK = flet.DataTable(heading_row_color=flet.Colors.BLUE_100,
                                          border=flet.Border(bottom=flet.BorderSide(2, flet.Colors.BLUE),
                                                             left=flet.BorderSide(2, flet.Colors.BLUE),
                                                             right=flet.BorderSide(2, flet.Colors.BLUE)),
                                          vertical_lines=flet.BorderSide(2, flet.Colors.BLUE),
                                          horizontal_lines=flet.BorderSide(10, flet.Colors.BLUE), columns=table_colums,
                                          rows=[])
            from db_data_perfom import platoky_data
            records = platoky_data()
            for record in records:
                data_tableMK.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text(record[0])),
                                                                 flet.DataCell(flet.Text(record[1])),
                                                                 flet.DataCell(flet.Text(record[2])),
                                                                 flet.DataCell(flet.Text(record[3])),
                                                                 flet.DataCell(flet.Text(record[4])),
                                                                 flet.DataCell(flet.Text(record[5])),
                                                                 flet.DataCell(flet.Text(record[6])),
                                                                 flet.DataCell(flet.Text(record[7])),
                                                                 flet.DataCell(flet.Text(record[8])),
                                                                 flet.DataCell(flet.Text(record[9])),
                                                                 flet.DataCell(flet.Text(record[10])),
                                                                 flet.DataCell(flet.Text(record[11])),
                                                                 flet.DataCell(flet.Text(record[12])),
                                                                 flet.DataCell(flet.Text(record[13])),
                                                                 flet.DataCell(flet.Text(record[14])),
                                                                 flet.DataCell(flet.Text(record[15])),
                                                                 flet.DataCell(flet.Text(record[16])),
                                                                 flet.DataCell(flet.Text(record[17])),
                                                                 flet.DataCell(flet.Text(record[18])),
                                                                 flet.DataCell(flet.Text(record[19])),
                                                                 flet.DataCell(flet.Text(record[20])),
                                                                 flet.DataCell(flet.Text(record[21])), ], ))
            data_tableMK.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text("~")),flet.DataCell(knopka_marketolog_na_glavnuju),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
                                                       flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")), ]))
            table_containerMK = flet.Column(controls=[flet.Row(controls=[data_tableMK], scroll=flet.ScrollMode.ALWAYS)],
                                          expand=True, scroll=flet.ScrollMode.ALWAYS)
            page.clean()
            page.add(table_containerMK)
        async def zurnalposech_MK_otrisovka(e):
            page.clean()
            page.add(table_containerMK2)
        async def knigaotzyv_MK_otrisovka(e):
            page.clean()
            page.add(table_containerMK3)
        async def vhod_validator(e):
            knopka_oshibki_vhoda.visible = False
            page.update()
            polzovatel_vvod = {}
            polzovatel_vvod["Имя_Пользователя"] = imja_polzovatelja.value
            polzovatel_vvod["Пароль"] = parol_polzovatelja.value
            try:
                polzak_valid=Polzovatel_Schema(**polzovatel_vvod)
                knopka_vhod.disabled=False
                page.update()
            except:
                knopka_vhod.disabled=True
                page.update()
        async def platok_validator(e):
            platok_s_flet_data = {}
            platok_s_flet_data["id"] = artikul_vvod.value
            platok_s_flet_data["Название_Платка"] = nazvanije_vvod.value
            platok_s_flet_data["Автор_Платка"] = avtor_vvod.value
            platok_s_flet_data["Колорит_1"] = kolorit_1_vvod.value
            platok_s_flet_data["Колорит_2"] = kolorit_2_vvod.value
            platok_s_flet_data["Колорит_3"] = kolorit_3_vvod.value
            platok_s_flet_data["Колорит_4"] = kolorit_4_vvod.value
            platok_s_flet_data["Колорит_5"] = kolorit_5_vvod.value
            platok_s_flet_data["Узор_Темени"] = uzor_temeni_vvod.value
            platok_s_flet_data["Узор_Сердцевины"] = uzor_sedceviny_vvod.value
            platok_s_flet_data["Узор_Сторон"] = uzor_storon_vvod.value
            platok_s_flet_data["Узор_Углов"] = uzor_uglov_vvod.value
            platok_s_flet_data["Узор_Края"] = uzor_kraja_vvod.value
            platok_s_flet_data["Цветы_Орнамент"] = cvety_ornament_vvod.value
            platok_s_flet_data["Изображённый_Цветок_1"] = cvetok_1_vvod.value
            platok_s_flet_data["Изображённый_Цветок_2"] = cvetok_2_vvod.value
            platok_s_flet_data["Изображённый_Цветок_3"] = cvetok_3_vvod.value
            platok_s_flet_data["Изображённый_Цветок_4"] = cvetok_4_vvod.value
            platok_s_flet_data["Изображённый_Цветок_5"] = cvetok_5_vvod.value
            platok_s_flet_data["Размер_Платка"] = platok_razmer_vvod.value
            platok_s_flet_data["Материал_Платка"] = platok_material_vvod.value
            platok_s_flet_data["Материал_Бахромы"] = platok_bahroma_vvod.value
            try:
                otpravka_knopka_fail.visible = False
                otpravka_knopka_success.visible = False
                otpravka_knopka_DBfail.visible = False
                otpravka_knopka_artoccup.visible = False
                otpravka_knopka_nameoccup.visible = False
                otpravka_knopka_DBsuccess.visible = False
                page.update()
                platok_kontroll = Platok_Schema(**platok_s_flet_data)
                otpravka_knopka.disabled=False
                otpravka_knopka_success.visible = True
                snack = page.snack_bar = flet.SnackBar(
                content=flet.Text("Данные проверены", color=flet.Colors.GREEN_ACCENT, size=28,
                                  weight=flet.FontWeight.W_100,
                                  font_family="Ponomar"), bgcolor=flet.Colors.GREEN) 
                page.show_dialog(snack)
                page.update()
            except ValidationError as e:
                otpravka_knopka_fail.visible = True
                snack = page.snack_bar = flet.SnackBar(
                content=flet.Text("Данные не прошли валидацию", color=cvet_1, size=28,
                                  weight=flet.FontWeight.BOLD,
                                  font_family="Ponomar"), bgcolor=cvet_2)
                page.show_dialog(snack)
                page.update()
            #uved=(
            #flet.AlertDialog(title="FAIL",visible=True)
            #
            #page.add(uved_kont)
        async def publikacija_vvod(e):
            publikacija_otpravka_knopka.disabled = True
            otpravka_knopka_fail.visible = False
            otpravka_knopka_success.visible = False
            otpravka_knopka_DBfail.visible = False
            otpravka_knopka_DBsuccess.visible = False
            stroka_data = str(2026) + "-" + vremja_publikacii_mesjac.value + "-" + vremja_publikacii_den.value + "T"
            stroka_data = stroka_data + vremja_publikacii_chas.value + ":" + vremja_publikacii_min.value
            page.update()
            publikacija_flet_data = {}
            publikacija_flet_data["Дата_публикации"]=stroka_data
            publikacija_flet_data["Текст_публикации"]=tekst_publikacii.value
            publikacija_flet_data["Ссылка_фото_публикации_1"]=foto_publikacii_1.value
            publikacija_flet_data["Ссылка_фото_публикации_2"] = foto_publikacii_2.value
            publikacija_flet_data["Ссылка_фото_публикации_3"] = foto_publikacii_3.value
            publikacija_flet_data["Ссылка_фото_публикации_4"] = foto_publikacii_4.value
            publikacija_flet_data["Ссылка_фото_публикации_5"] = foto_publikacii_5.value
            publikacija_flet_data["Ссылка_на_сайт_с_материалом"]=material_publikacii.value
            publikacija_flet_data["Ссылка_на_документ_с_материалом"]=ssylka_publikacii.value
            sost_vvoda_publikacii=await vvod_publikacii(publikacija_flet_data)
            if sost_vvoda_publikacii==0:
                otpravka_knopka_DBsuccess.visible = True
                snack = page.snack_bar = flet.SnackBar(
                content=flet.Text("ЗАПИСЬ УСПЕШНО ДОБАВЛЕНА", color=flet.Colors.GREEN, size=28,
                                  weight=flet.FontWeight.W_100,font_family="Ponomar"), bgcolor=flet.Colors.GREEN_ACCENT)
                page.show_dialog(snack)
                message_plain=""
                message_plain= message_plain + "Дата_публикации" + ":" + " " + stroka_data + ";" + " "
                message_plain= message_plain + "Текст_публикации" + ":" + " " + tekst_publikacii.value + ";" + " "
                message_plain = message_plain + "Ссылка_фото_публикации_1" + ":" + " " + foto_publikacii_1.value + ";" + " "
                message_plain = message_plain + "Ссылка_фото_публикации_2" + ":" + " " + foto_publikacii_2.value + ";" + " "
                message_plain = message_plain + "Ссылка_фото_публикации_3" + ":" + " " + foto_publikacii_3.value + ";" + " "
                message_plain = message_plain + "Ссылка_фото_публикации_4" + ":" + " " + foto_publikacii_4.value + ";" + " "
                message_plain = message_plain + "Ссылка_фото_публикации_5" + ":" + " " + foto_publikacii_5.value + ";" + " "
                message_plain = message_plain + "Ссылка_на_сайт_с_материалом" + ":" + " " + ssylka_publikacii.value
                message_plain = message_plain + "Ссылка_на_документ_с_материалом" + ":" + " " + material_publikacii.value
                vremja_publikacii_min.value=""
                vremja_publikacii_chas.value=""
                vremja_publikacii_mesjac.value=""
                vremja_publikacii_den.value=""
                tekst_publikacii.value=""
                foto_publikacii_1.value=""
                foto_publikacii_2.value = ""
                foto_publikacii_3.value = ""
                foto_publikacii_4.value = ""
                foto_publikacii_5.value = ""
                ssylka_publikacii.value= ""
                material_publikacii.value= ""
                page.update()
                asyncio.create_task(opovestitel_publikacii(message_plain))
            if sost_vvoda_publikacii ==1:
                snack = page.snack_bar = flet.SnackBar(
                content=flet.Text("БАЗА ДАННЫХ НЕИСПРАВНА", color=flet.Colors.PURPLE_ACCENT, size=28,
                                      weight=flet.FontWeight.W_100,
                                      font_family="Ponomar"), bgcolor=flet.Colors.RED)
                page.show_dialog(snack)
                otpravka_knopka_DBfail.visible=True
                page.update()
        async def publikacija_validator(e):
            try:
                otpravka_knopka_fail.visible = False
                otpravka_knopka_success.visible = False
                otpravka_knopka_DBsuccess.visible = False
                otpravka_knopka_DBfail.visible = False
                page.update()
                stroka_data=str(2026)+"-"+vremja_publikacii_mesjac.value+"-"+vremja_publikacii_den.value+"T"
                stroka_data=stroka_data+vremja_publikacii_chas.value+":"+vremja_publikacii_min.value
                publikacija_flet_data={}
                publikacija_flet_data["Дата_Время_Публикации"]=stroka_data
                publikacija_flet_data["Ссылка_фото_публикации_1"]=foto_publikacii_1.value
                publikacija_flet_data["Ссылка_фото_публикации_2"] = foto_publikacii_2.value
                publikacija_flet_data["Ссылка_фото_публикации_3"] = foto_publikacii_3.value
                publikacija_flet_data["Ссылка_фото_публикации_4"] = foto_publikacii_4.value
                publikacija_flet_data["Ссылка_фото_публикации_5"] = foto_publikacii_5.value
                publikacija_flet_data["Ссылка_на_сайт_с_материалом"]=ssylka_publikacii.value
                publikacija_flet_data["Ссылка_на_документ_с_материалом"]=material_publikacii.value
                publikacija_flet_data["Текст_публикации"] = tekst_publikacii.value
                proverka_publikacija=Publikacii_Schema(**publikacija_flet_data)
                snack = page.snack_bar = flet.SnackBar(
                content=flet.Text("Данные проверены", color=flet.Colors.GREEN_ACCENT, size=28,
                                  weight=flet.FontWeight.W_100,
                                  font_family="Ponomar"), bgcolor=flet.Colors.GREEN)
                otpravka_knopka_success.visible = True
                publikacija_otpravka_knopka.disabled =  False
                page.show_dialog(snack)
                page.update()
            except:
                otpravka_knopka_fail.visible = True
                publikacija_otpravka_knopka.disabled = True
                snack = page.snack_bar = flet.SnackBar(
                content=flet.Text("Данные не прошли валидацию", color=cvet_1, size=28,
                                  weight=flet.FontWeight.BOLD,
                                  font_family="Ponomar"), bgcolor=cvet_2)
                page.show_dialog(snack)
                page.update()
        async def platok_vvod(e):
            otpravka_knopka.disabled=True
            otpravka_knopka_fail.visible = False
            otpravka_knopka_success.visible = False
            otpravka_knopka_DBfail.visible = False
            otpravka_knopka_artoccup.visible = False
            otpravka_knopka_nameoccup.visible = False
            otpravka_knopka_DBsuccess.visible=False
            page.update()
            platok_s_flet_data = {}
            platok_s_flet_data["id"] = artikul_vvod.value
            platok_s_flet_data["Название_Платка"] = nazvanije_vvod.value
            platok_s_flet_data["Автор_Платка"] = avtor_vvod.value
            platok_s_flet_data["Колорит_1"] = kolorit_1_vvod.value
            platok_s_flet_data["Колорит_2"] = kolorit_2_vvod.value
            platok_s_flet_data["Колорит_3"] = kolorit_3_vvod.value
            platok_s_flet_data["Колорит_4"] = kolorit_4_vvod.value
            platok_s_flet_data["Колорит_5"] = kolorit_5_vvod.value
            platok_s_flet_data["Узор_Темени"] = uzor_temeni_vvod.value
            platok_s_flet_data["Узор_Сердцевины"] = uzor_sedceviny_vvod.value
            platok_s_flet_data["Узор_Сторон"] = uzor_storon_vvod.value
            platok_s_flet_data["Узор_Углов"] = uzor_uglov_vvod.value
            platok_s_flet_data["Узор_Края"] = uzor_kraja_vvod.value
            platok_s_flet_data["Цветы_Орнамент"] = cvety_ornament_vvod.value
            platok_s_flet_data["Изображённый_Цветок_1"] = cvetok_1_vvod.value
            platok_s_flet_data["Изображённый_Цветок_2"] = cvetok_2_vvod.value
            platok_s_flet_data["Изображённый_Цветок_3"] = cvetok_3_vvod.value
            platok_s_flet_data["Изображённый_Цветок_4"] = cvetok_4_vvod.value
            platok_s_flet_data["Изображённый_Цветок_5"] = cvetok_5_vvod.value
            platok_s_flet_data["Размер_Платка"] = platok_razmer_vvod.value
            platok_s_flet_data["Материал_Платка"] = platok_material_vvod.value
            platok_s_flet_data["Материал_Бахромы"] = platok_bahroma_vvod.value
            vvod_sost=await vvod_platka(platok_s_flet_data)
            if vvod_sost==0:
                otpravka_knopka_DBfail.visible = True
                snack = page.snack_bar = flet.SnackBar(
                content=flet.Text("БАЗА ДАННЫХ НЕИСПРАВНА", color=flet.Colors.PURPLE_ACCENT, size=28,
                                  weight=flet.FontWeight.W_100,
                                  font_family="Ponomar"), bgcolor=flet.Colors.RED)
                page.show_dialog(snack)
                page.update()
            elif vvod_sost==1:
                otpravka_knopka_artoccup.visible = True
                snack = page.snack_bar = flet.SnackBar(
                content=flet.Text("АРТИКУЛ ЗАНЯТ", color=cvet_1, size=28,
                                  weight=flet.FontWeight.W_100,
                                  font_family="Ponomar"), bgcolor=cvet_2)
                page.show_dialog(snack)
                page.update()
            elif vvod_sost==2:
                otpravka_knopka_nameoccup.visible = True
                snack = page.snack_bar = flet.SnackBar(
                content=flet.Text("ТАКОЙ ПЛАТОК УЖЕ ЕСТЬ", color=cvet_1, size=28,
                                  weight=flet.FontWeight.W_100,
                                  font_family="Ponomar"), bgcolor=cvet_2)
                page.show_dialog(snack)
                page.update()
            elif vvod_sost==3:
                snack = page.snack_bar = flet.SnackBar(
                content=flet.Text("ЗАПИСЬ УСПЕШНО ДОБАВЛЕНА", color=flet.Colors.GREEN, size=28,
                                  weight=flet.FontWeight.W_100,
                                  font_family="Ponomar"), bgcolor=flet.Colors.GREEN_ACCENT)
                page.show_dialog(snack)
                otpravka_knopka_DBsuccess.visible = True
                message_plain = ""
                message_plain = message_plain + "id:" + " " + artikul_vvod.value + ";" + " "
                message_plain = message_plain + "Название платка:" + " " + nazvanije_vvod.value + ";" + " "
                message_plain = message_plain + "Автор платка:" + " " + avtor_vvod.value + ";" + " "
                message_plain = message_plain + "Вариант окраски 1:" + " " + kolorit_1_vvod.value + ";" + " "
                message_plain = message_plain + "Вариант окраски 2:" + " " + kolorit_2_vvod.value + ";" + " "
                message_plain = message_plain + "Вариант окраски 3:" + " " + kolorit_3_vvod.value + ";" + " "
                message_plain = message_plain + "Вариант окраски 4:" + " " + kolorit_4_vvod.value + ";" + " "
                message_plain = message_plain + "Вариант окраски 5:" + " " + kolorit_5_vvod.value + ";" + " "
                message_plain = message_plain + "Узор темени:" + " " + uzor_temeni_vvod.value + ";" + " "
                message_plain = message_plain + "Узор сердцевины:" + " " + uzor_sedceviny_vvod.value + ";" + " "
                message_plain = message_plain + "Узор сторон:" + " " + uzor_storon_vvod.value + ";" + " "
                message_plain = message_plain + "Узор углов:" + " " + uzor_uglov_vvod.value + ";" + " "
                message_plain = message_plain + "Узор края:" + " " + uzor_kraja_vvod.value + ";" + " "
                message_plain = message_plain + "Соотношение цветов и узора:" + " " + cvety_ornament_vvod.value + ";" + " "
                message_plain = message_plain + "Нарисованный цветок 1:" + " " + cvetok_1_vvod.value + ";" + " "
                message_plain = message_plain + "Нарисованный цветок 2:" + " " + cvetok_2_vvod.value + ";" + " "
                message_plain = message_plain + "Нарисованный цветок 3:" + " " + cvetok_3_vvod.value + ";" + " "
                message_plain = message_plain + "Нарисованный цветок 4:" + " " + cvetok_4_vvod.value + ";" + " "
                message_plain = message_plain + "Нарисованный цветок 5:" + " " + cvetok_5_vvod.value + ";" + " "
                message_plain = message_plain + "Размер платка:" + " " + platok_razmer_vvod.value + ";" + " "
                message_plain = message_plain + "Материал платка:" + " " + platok_material_vvod.value + ";" + " "
                message_plain = message_plain + "Материал бахромы:" + " " + platok_bahroma_vvod.value
                artikul_vvod.value = ""
                nazvanije_vvod.value = ""
                avtor_vvod.value = ""
                kolorit_1_vvod.value = ""
                kolorit_2_vvod.value = ""
                kolorit_3_vvod.value = ""
                kolorit_4_vvod.value = ""
                kolorit_5_vvod.value = ""
                uzor_temeni_vvod.value = ""
                uzor_sedceviny_vvod.value = ""
                uzor_storon_vvod.value = ""
                uzor_uglov_vvod.value = ""
                uzor_kraja_vvod.value = ""
                cvety_ornament_vvod.value = ""
                cvetok_1_vvod.value = ""
                cvetok_2_vvod.value = ""
                cvetok_3_vvod.value = ""
                cvetok_4_vvod.value = ""
                cvetok_5_vvod.value = ""
                platok_razmer_vvod.value = ""
                platok_material_vvod.value = ""
                platok_bahroma_vvod.value = ""
                page.update()
                asyncio.create_task(opovestitel(message_plain))
        def pustyshka(e):
            print(e)
            page.update()
        #поля_ввода публикации
        vremja_publikacii_chas=flet.TextField(text_size=razmer_bukov, label="Время публикации,ЧАСЫ", color=cvet_1,
                                  text_style=flet.TextStyle(font_family="Arial", size=razmer_bukov - 4, color=cvet_1),
                                  label_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov -2, color=cvet_1),
                                  cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                  on_blur=publikacija_validator)
        vremja_publikacii_min=flet.TextField(text_size=razmer_bukov, label="Время публикации,МИН", color=cvet_1,
                                  text_style=flet.TextStyle(font_family="Arial", size=razmer_bukov - 4, color=cvet_1),
                                  label_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov -2, color=cvet_1),
                                  cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                  on_blur=publikacija_validator)
        vremja_publikacii_den=flet.TextField(text_size=razmer_bukov, label="Дата публикации,ДЕНЬ", color=cvet_1,
                                  text_style=flet.TextStyle(font_family="Arial", size=razmer_bukov - 2, color=cvet_1),
                                  label_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov, color=cvet_1),
                                  cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                  on_blur=publikacija_validator)
        vremja_publikacii_mesjac=flet.TextField(text_size=razmer_bukov, label="Дата публикации,МЕСЯЦ", color=cvet_1,
                                  text_style=flet.TextStyle(font_family="Arial", size=razmer_bukov - 2, color=cvet_1),
                                  label_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov, color=cvet_1),
                                  cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                  on_blur=publikacija_validator)
        tekst_publikacii = flet.TextField(text_size=razmer_bukov, height=500,label="Текст публикации", color=cvet_1,
                                              text_style=flet.TextStyle(font_family="Arial", size=razmer_bukov - 6,
                                                                        color=cvet_1),
                                              label_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov,
                                                                         color=cvet_1),
                                              cursor_color=cvet_1, border_color=cvet_2,
                                              on_blur=publikacija_validator,multiline=True,min_lines=60)
        foto_publikacii_1 = flet.TextField(text_size=razmer_bukov, label="Ссылка на фото 1", color=cvet_1,
                                      text_style=flet.TextStyle(font_family="Arial", size=razmer_bukov - 2,
                                                                color=cvet_1),
                                      label_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov,
                                                                 color=cvet_1),
                                      cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                      on_blur=publikacija_validator)
        foto_publikacii_2 = flet.TextField(text_size=razmer_bukov, label="Ссылка на фото 2", color=cvet_1,
                                       text_style=flet.TextStyle(font_family="Arial", size=razmer_bukov - 2,
                                                                 color=cvet_1),
                                       label_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov,
                                                                  color=cvet_1),
                                       cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                       on_blur=publikacija_validator)
        foto_publikacii_3 = flet.TextField(text_size=razmer_bukov, label="Ссылка на фото 3", color=cvet_1,
                                       text_style=flet.TextStyle(font_family="Arial", size=razmer_bukov - 2,
                                                                 color=cvet_1),
                                       label_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov,
                                                                  color=cvet_1),
                                       cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                       on_blur=publikacija_validator)
        foto_publikacii_4 = flet.TextField(text_size=razmer_bukov, label="Ссылка на фото 4", color=cvet_1,
                                       text_style=flet.TextStyle(font_family="Arial", size=razmer_bukov - 2,
                                                                 color=cvet_1),
                                       label_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov,
                                                                  color=cvet_1),
                                       cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                       on_blur=publikacija_validator)
        foto_publikacii_5 = flet.TextField(text_size=razmer_bukov, label="Ссылка на фото 5", color=cvet_1,
                                       text_style=flet.TextStyle(font_family="Arial", size=razmer_bukov - 2,
                                                                 color=cvet_1),
                                       label_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov,
                                                                  color=cvet_1),
                                       cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                       on_blur=publikacija_validator)
        ssylka_publikacii = flet.TextField(text_size=razmer_bukov, label="Интернет-ссылка", color=cvet_1,
                                       text_style=flet.TextStyle(font_family="Arial", size=razmer_bukov - 2,
                                                                 color=cvet_1),
                                       label_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov,
                                                                  color=cvet_1),
                                       cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                       on_blur=publikacija_validator)
        material_publikacii = flet.TextField(text_size=razmer_bukov, label="ID-вложения", color=cvet_1,
                                       text_style=flet.TextStyle(font_family="Arial", size=razmer_bukov - 2,
                                                                 color=cvet_1),
                                       label_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov,
                                                                  color=cvet_1),
                                       cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                       on_blur=publikacija_validator)
        #поля_ввода платка
        artikul_vvod = flet.TextField(text_size=razmer_bukov, label="Артикул", color=cvet_1,
                                  text_style=flet.TextStyle(font_family="Arial", size=razmer_bukov - 2, color=cvet_1),
                                  label_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov, color=cvet_1),
                                  cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                  on_blur=platok_validator)
        nazvanije_vvod = flet.TextField(label="Название", color=cvet_1,
                                    label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                    text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2,
                                                              color=cvet_1),
                                    cursor_color=cvet_1, border_color=cvet_2, border_radius=100,
                                    on_blur=platok_validator)
        avtor_vvod = flet.TextField(label="Автор", color=cvet_1,
                                label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2, color=cvet_1),
                                cursor_color=cvet_1, border_radius=100, border_color=cvet_2, on_blur=platok_validator)
        kolorit_1_vvod = flet.TextField(label="Колорит 1", color=cvet_1,
                                    label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                    text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2,
                                                              color=cvet_1),
                                    cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                    on_blur=platok_validator)
        kolorit_2_vvod = flet.TextField(label="Колорит 2", color=cvet_1,
                                    label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                    text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2,
                                                              color=cvet_1),
                                    cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                    on_blur=platok_validator)
        kolorit_3_vvod = flet.TextField(label="Колорит 3", color=cvet_1,
                                    label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                    text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2,
                                                              color=cvet_1),
                                    cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                    on_blur=platok_validator)
        kolorit_4_vvod = flet.TextField(label="Колорит 4", color=cvet_1,
                                    label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                    text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2,
                                                              color=cvet_1),
                                    cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                    on_blur=platok_validator)
        kolorit_5_vvod = flet.TextField(label="Колорит 5", color=cvet_1,
                                    label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                    text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2,
                                                              color=cvet_1),
                                    cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                    on_blur=platok_validator)
        uzor_temeni_vvod = flet.TextField(label="Узор темени", color=cvet_1,
                                      label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                      text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2,
                                                                color=cvet_1),
                                      cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                      on_blur=platok_validator)
        uzor_sedceviny_vvod = flet.TextField(label="Узор сердцевины", color=cvet_1,
                                         label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                         text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2,
                                                                   color=cvet_1),
                                         cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                         on_blur=platok_validator)
        uzor_storon_vvod = flet.TextField(label="Узор сторон", color=cvet_1,
                                      label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                      cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                      text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2,
                                                                color=cvet_1),
                                      on_blur=platok_validator)
        uzor_uglov_vvod = flet.TextField(label="Узор углов", color=cvet_1,
                                     label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                     text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2,
                                                               color=cvet_1),
                                     cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                     on_blur=platok_validator)
        uzor_kraja_vvod = flet.TextField(label="Узор краёв", color=cvet_1,
                                     label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                     text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2,
                                                               color=cvet_1),
                                     cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                     on_blur=platok_validator)
        cvety_ornament_vvod = flet.TextField(label="Соотношение рисунка и орнамента", color=cvet_1,
                                         label_style=flet.TextStyle(size=razmer_bukov - 3, color=cvet_1),
                                         text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2,
                                                                   color=cvet_1),
                                         cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                         on_blur=platok_validator)
        cvetok_1_vvod = flet.TextField(label="Нарисованный цветок 1", color=cvet_1,
                                   label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                   text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2,
                                                             color=cvet_1),
                                   cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                   on_blur=platok_validator)
        cvetok_2_vvod = flet.TextField(label="Нарисованный цветок 2", color=cvet_1,
                                   label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                   text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2,
                                                             color=cvet_1),
                                   cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                   on_blur=platok_validator)
        cvetok_3_vvod = flet.TextField(label="Нарисованный цветок 3", color=cvet_1,
                                   label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                   text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2,
                                                             color=cvet_1),
                                   cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                   on_blur=platok_validator)
        cvetok_4_vvod = flet.TextField(label="Нарисованный цветок 4", color=cvet_1,
                                   label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                   text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2,
                                                             color=cvet_1),
                                   cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                   on_blur=platok_validator)
        cvetok_5_vvod = flet.TextField(label="Нарисованный цветок 5", color=cvet_1,
                                   label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                   text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2,
                                                             color=cvet_1),
                                   cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                   on_blur=platok_validator)
        platok_razmer_vvod = flet.TextField(label="Размер платка", color=cvet_1,
                                        label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                        text_style=flet.TextStyle(font_family="Arial", size=razmer_bukov - 2,
                                                                  color=cvet_1),
                                        cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                        on_blur=platok_validator)
        platok_material_vvod = flet.TextField(label="Материал платка", color=cvet_1,
                                          label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                          text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2,
                                                                    color=cvet_1),
                                          cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                          on_blur=platok_validator)
        platok_bahroma_vvod = flet.TextField(label="Материал бахромы", color=cvet_1,
                                         label_style=flet.TextStyle(size=razmer_bukov, color=cvet_1),
                                         text_style=flet.TextStyle(font_family="Ponomar", size=razmer_bukov - 2,
                                                                   color=cvet_1),
                                         cursor_color=cvet_1, border_radius=100, border_color=cvet_2,
                                         on_blur=platok_validator)
        otpravka_knopka = flet.FilledButton("ОТПРАВИТЬ ЗАПИСЬ В БД",width=400, height=60,on_click=platok_vvod, disabled=True, visible=True,
                                  style=flet.ButtonStyle(color=cvet_1, bgcolor=cvet_2))
        publikacija_otpravka_knopka = flet.FilledButton("ОТПРАВИТЬ ЗАПИСЬ В БД", width=400, height=60, on_click=publikacija_vvod,
                                                    disabled=True, visible=True,
                                        style=flet.ButtonStyle(color=cvet_1, bgcolor=cvet_2))
        otpravka_knopka_fail = flet.FilledButton("ДАННЫЕ НЕ ПРОШЛИ ВАЛИДАЦИЮ", width=400, height=40, on_click=pustyshka,
                                        disabled=True, visible=False,
                                        style=flet.ButtonStyle(color=cvet_1, bgcolor=cvet_2))
        otpravka_knopka_success = flet.FilledButton("ДАННЫЕ ПРОВЕРЕНЫ", width=400, height=40, on_click=pustyshka,
                                             disabled=True, visible=False,
                                             style=flet.ButtonStyle(color=flet.Colors.GREEN, bgcolor=flet.Colors.GREEN_ACCENT))
        otpravka_knopka_DBfail = flet.FilledButton("НЕИСПРАВНОСТЬ БАЗЫ ДАННЫХ", width=400, height=40, on_click=pustyshka,
                                                disabled=True, visible=False,
                                                style=flet.ButtonStyle(color=flet.Colors.RED,
                                                                       bgcolor=flet.Colors.PURPLE))
        otpravka_knopka_artoccup = flet.FilledButton("АРТИКУЛ ЗАНЯТ", width=400, height=40, on_click=pustyshka,
                                               disabled=True, visible=False,
                                               style=flet.ButtonStyle(color=cvet_1, bgcolor=cvet_2))
        otpravka_knopka_nameoccup = flet.FilledButton("ТАКОЙ ПЛАТОК УЖЕ ЕСТЬ", width=400, height=40, on_click=pustyshka,
                                                 disabled=True, visible=False,
                                                 style=flet.ButtonStyle(color=cvet_1, bgcolor=cvet_2))
        otpravka_knopka_DBsuccess = flet.FilledButton("ЗАПИСЬ УСПЕШНО ДОБАВЛЕНА", width=400, height=40, on_click=pustyshka,
                                                  disabled=True, visible=False,
                                                  style=flet.ButtonStyle(color=flet.Colors.GREEN, bgcolor=flet.Colors.GREEN_ACCENT))
        knopka_publikacija_glavnaja = flet.FilledButton("НАЗАД НА ГЛАВНУЮ", width=400, height=60,
                                                        on_click=glavnaja_otrisovka,
                                                        disabled=False, visible=True,
                                                        style=flet.ButtonStyle(color=flet.Colors.BLUE_50,
                                                                               bgcolor=flet.Colors.BLUE))
        knopka_platok_glavnaja = flet.FilledButton("НАЗАД НА ГЛАВНУЮ", width=400, height=60,
                                                   on_click=glavnaja_otrisovka,
                                                   disabled=False, visible=True,
                                                   style=flet.ButtonStyle(color=flet.Colors.BLUE_50,
                                                                          bgcolor=flet.Colors.BLUE))
        knopka_glavnaja_platok = flet.FilledButton("ВВЕСТИ ДАННЫЕ О ПЛАТКЕ", width=375, height=60, on_click=platok_otrisovka,
                                               disabled=False, visible=True,
                                               style=flet.ButtonStyle(color=flet.Colors.RED,
                                                                       bgcolor=flet.Colors.PURPLE))
        knopka_glavnaja_publikacija = flet.FilledButton("ЗАПЛАНИРОВАТЬ ПУБЛИКАЦИЮ", width=375, height=60,
                                               on_click=publikacija_otrisovka,
                                               disabled=False, visible=True,
                                               style=flet.ButtonStyle(color=flet.Colors.RED,
                                                                      bgcolor=flet.Colors.PURPLE))
        knopka_glavnaja_bazadannyh = flet.FilledButton("ПЛАТОЧНАЯ БАЗА ДАННЫХ", width=375, height=60,
                                                    on_click=bazadannyh_otrisovka,
                                                    disabled=False, visible=True,
                                                    style=flet.ButtonStyle(color=flet.Colors.RED,
                                                                           bgcolor=flet.Colors.PURPLE))
        knopka_glavnaja_bazadannyh_teh = flet.FilledButton("ПЛАТОЧНАЯ БАЗА ДАННЫХ", width=375, height=60,
                                                       on_click=bazadannyh_Teh_otrisovka,
                                                       disabled=False, visible=True,
                                                       style=flet.ButtonStyle(color=flet.Colors.RED,
                                                                              bgcolor=flet.Colors.PURPLE))
        knopka_glavnaja_bazadannyh_prod = flet.FilledButton("ПЛАТОЧНАЯ БАЗА ДАННЫХ", width=375, height=60,
                                                           on_click=bazadannyh_PR_otrisovka,
                                                           disabled=False, visible=True,
                                                           style=flet.ButtonStyle(color=flet.Colors.RED,
                                                                                  bgcolor=flet.Colors.PURPLE))
        knopka_glavnaja_bazadannyh_market = flet.FilledButton("ПЛАТОЧНАЯ БАЗА ДАННЫХ", width=375, height=60,
                                                            on_click=bazadannyh_MK_otrisovka,
                                                            disabled=False, visible=True,
                                                            style=flet.ButtonStyle(color=flet.Colors.RED,
                                                                                   bgcolor=flet.Colors.PURPLE))
        knopka_zurnal_posezhenija = flet.FilledButton("ЖУРНАЛ ПОСЕЩЕНИЙ", width=375, height=60,
                                                       on_click=zurnalposech_otrisovka,
                                                       disabled=False, visible=True,
                                                       style=flet.ButtonStyle(color=flet.Colors.RED,
                                                                              bgcolor=flet.Colors.PURPLE))
        knopka_zurnal_posezhenija_teh = flet.FilledButton("ЖУРНАЛ ПОСЕЩЕНИЙ", width=375, height=60,
                                                      on_click=zurnalposech_Teh_otrisovka,
                                                      disabled=False, visible=True,
                                                      style=flet.ButtonStyle(color=flet.Colors.RED,
                                                                             bgcolor=flet.Colors.PURPLE))
        knopka_zurnal_posezhenija_prod = flet.FilledButton("ЖУРНАЛ ПОСЕЩЕНИЙ", width=375, height=60,
                                                          on_click=zurnalposech_PR_otrisovka,
                                                          disabled=False, visible=True,
                                                          style=flet.ButtonStyle(color=flet.Colors.RED,
                                                                                 bgcolor=flet.Colors.PURPLE))
        knopka_zurnal_posezhenija_market = flet.FilledButton("ЖУРНАЛ ПОСЕЩЕНИЙ", width=375, height=60,
                                                           on_click=zurnalposech_MK_otrisovka,
                                                           disabled=False, visible=True,
                                                           style=flet.ButtonStyle(color=flet.Colors.RED,
                                                                                  bgcolor=flet.Colors.PURPLE))
        knopka_kniga_posezhenija = flet.FilledButton("КНИГА ОТЗЫВОВ", width=375, height=60,
                                                      on_click=knigaotzyv_otrisovka,
                                                      disabled=False, visible=True,
                                                      style=flet.ButtonStyle(color=flet.Colors.RED,
                                                                             bgcolor=flet.Colors.PURPLE))
        knopka_kniga_posezhenija_teh = flet.FilledButton("КНИГА ОТЗЫВОВ", width=375, height=60,
                                                     on_click=knigaotzyv_Teh_otrisovka,
                                                     disabled=False, visible=True,
                                                     style=flet.ButtonStyle(color=flet.Colors.RED,
                                                                            bgcolor=flet.Colors.PURPLE))
        knopka_kniga_posezhenija_market = flet.FilledButton("КНИГА ОТЗЫВОВ", width=375, height=60,
                                                         on_click=knigaotzyv_MK_otrisovka,
                                                         disabled=False, visible=True,
                                                         style=flet.ButtonStyle(color=flet.Colors.RED,
                                                                                bgcolor=flet.Colors.PURPLE))
        knopka_kniga_posezhenija_prod = flet.FilledButton("КНИГА ОТЗЫВОВ", width=375, height=60,
                                                            on_click=knigaotzyv_PR_otrisovka,
                                                            disabled=False, visible=True,
                                                            style=flet.ButtonStyle(color=flet.Colors.RED,
                                                                                   bgcolor=flet.Colors.PURPLE))
        knopka_vyhod = flet.FilledButton("ВЫХОД", width=400, height=60, on_click=posle_vyhoda,
                                            disabled=False, visible=True,
                                            style=flet.ButtonStyle(color=cvet_1, bgcolor=cvet_2))
        knopka_prozhanije_1 = flet.FilledButton("СПАСИБО ЗА РАБОТУ", width=400, height=60, on_click=pustyshka,
                                         disabled=False, visible=True,
                                         style=flet.ButtonStyle(color=cvet_1, bgcolor=cvet_2))
        knopka_prozhanije_2 = flet.FilledButton("АНГЕЛА ХРАНИТЕЛЯ", width=400, height=60, on_click=pustyshka,
                                                disabled=False, visible=True,
                                                style=flet.ButtonStyle(color=cvet_1, bgcolor=cvet_2))
        knopka_prozhanije_3 = flet.FilledButton("НАЗАД НА www.platoky.ee", width=400, height=60, on_click=na_glavnuju,
                                                disabled=False, visible=True,
                                                style=flet.ButtonStyle(color=cvet_1, bgcolor=cvet_2))
        knopka_prozhanije_4 = flet.FilledButton("Авторизоваться снова", width=400, height=60, on_click=panel_vhoda,
                                                disabled=False, visible=True,
                                                style=flet.ButtonStyle(color=cvet_1, bgcolor=cvet_2))

        form_container_1 = flet.Container(width=275, height=900, top=50, left=215,
                                      content=flet.Column([flet.Text("Ввести новый платок", color=cvet_1, size=28,
                                                                     weight=flet.FontWeight.BOLD,
                                                                     font_family="Ponomar"),
                                                           artikul_vvod, nazvanije_vvod, avtor_vvod, kolorit_1_vvod,
                                                           kolorit_2_vvod, kolorit_3_vvod, kolorit_4_vvod,
                                                           kolorit_5_vvod,
                                                           uzor_temeni_vvod, uzor_sedceviny_vvod, uzor_storon_vvod,
                                                           uzor_uglov_vvod, uzor_kraja_vvod,
                                                           ], ))
        form_container_2 = flet.Container(width=280, height=575, top=102, left=495, content=flet.Column([
        cvety_ornament_vvod, cvetok_1_vvod, cvetok_2_vvod, cvetok_3_vvod, cvetok_4_vvod, cvetok_5_vvod,
        platok_razmer_vvod,
        platok_material_vvod, platok_bahroma_vvod], ))
        form_container_3 = flet.Container(width=280, height=600, top=705, left=495, content=flet.Column([otpravka_knopka], ))
        form_container_4 = flet.Container(width=280, height=50, top=45, left=495,
                                      content=flet.Column([otpravka_knopka_fail], ))
        form_container_5 = flet.Container(width=280, height=50, top=45, left=495,
                                      content=flet.Column([otpravka_knopka_success], ))
        form_container_6 = flet.Container(width=280, height=50, top=45, left=495,
                                      content=flet.Column([otpravka_knopka_DBfail], ))
        form_container_7 = flet.Container(width=280, height=50, top=45, left=495,
                                      content=flet.Column([otpravka_knopka_artoccup], ))
        form_container_8 = flet.Container(width=280, height=50, top=45, left=495,
                                      content=flet.Column([otpravka_knopka_nameoccup], ))
        form_container_9 = flet.Container(width=280, height=50, top=45, left=495,
                                      content=flet.Column([otpravka_knopka_DBsuccess], ))
        form_container_10 = flet.Container(width=500, height=900, top=10, left=175,
                                      content=flet.Column([flet.Text("Плановая публикация", color=cvet_1, size=28,
                                                                     weight=flet.FontWeight.BOLD,
                                                                     font_family="Ponomar"),vremja_publikacii_chas,
                                                           vremja_publikacii_min,
                                                           vremja_publikacii_den,
                                                           vremja_publikacii_mesjac,
                                                           foto_publikacii_1,
                                                           foto_publikacii_2, foto_publikacii_3, foto_publikacii_4,
                                                           foto_publikacii_5, material_publikacii,
                                                           ssylka_publikacii
                                                           ], ))
        form_container_11 = flet.Container(width=700, height=900, top=100, left=490,
                                       content=flet.Column([tekst_publikacii], ))
        form_container_12 = flet.Container(width=280, height=50, top=45, left=495,
                                      content=flet.Column([otpravka_knopka_DBsuccess], ))
        form_container_13 = flet.Container(width=280, height=50, top=620, left=495,
                                      content=flet.Column([publikacija_otpravka_knopka], ))
        form_container_14 = flet.Container(width=280, height=50, top=691, left=495,
                                       content=flet.Column([knopka_publikacija_glavnaja], ))
        form_container_15 = flet.Container(width=280, height=50, top=772, left=495,
                                       content=flet.Column([knopka_platok_glavnaja], ))
        #ОБОРАЧИВАНИЕ КНОПОК В КОНТЕЙНЕР
        form_container_16 = flet.Container(width=280, height=400, top=125, left=15,
                                       content=flet.Column([knopka_glavnaja_platok], ))
        container_knopka_bazzadannyh_PR=flet.Container(width=280, height=400, top=125, left=15,
                                       content=flet.Column([knopka_glavnaja_bazadannyh_prod], ))
        container_knopka_bazzadannyh_TH = flet.Container(width=280, height=400, top=125, left=15,
                                                         content=flet.Column([knopka_glavnaja_bazadannyh_teh], ))
        container_knopka_bazzadannyh_MK = flet.Container(width=280, height=400, top=125, left=15,
                                                         content=flet.Column([knopka_glavnaja_bazadannyh_market], ))
        form_container_17 = flet.Container(width=280, height=400, top=225, left=15,
                                       content=flet.Column([knopka_glavnaja_publikacija], ))
        form_container_18 = flet.Container(width=280, height=400, top=325, left=15,
                                       content=flet.Column([knopka_glavnaja_bazadannyh], ))
        form_container_24 = flet.Container(width=280, height=400, top=425, left=15,
                                           content=flet.Column([knopka_zurnal_posezhenija], ))
        container_knopka_zurnalpos_PR=flet.Container(width=280, height=400, top=225, left=15,
                                       content=flet.Column([knopka_zurnal_posezhenija_prod], ))
        container_knopka_zurnalpos_TH = flet.Container(width=280, height=400, top=225, left=15,
                                                       content=flet.Column([knopka_zurnal_posezhenija_teh], ))
        container_knopka_zurnalpos_MK = flet.Container(width=280, height=400, top=225, left=15,
                                                       content=flet.Column([knopka_zurnal_posezhenija_market], ))
        form_container_25 = flet.Container(width=280, height=400, top=525, left=15,
                                           content=flet.Column([knopka_kniga_posezhenija], ))
        container_kniga_posezhenija_PR = flet.Container(width=280, height=400, top=325, left=15,
                                                       content=flet.Column([knopka_kniga_posezhenija_prod], ))
        container_kniga_posezhenija_TH = flet.Container(width=280, height=400, top=325, left=15,
                                                        content=flet.Column([knopka_kniga_posezhenija_teh], ))
        container_kniga_posezhenija_MK = flet.Container(width=280, height=400, top=325, left=15,
                                                        content=flet.Column([knopka_kniga_posezhenija_market], ))
        form_container_26 = flet.Container(width=280, height=400, top=625, left=15,
                                           content=flet.Column([knopka_vyhod], ))
        form_container_27 = flet.Container(width=280, height=400, top=175, left=15,
                                           content=flet.Column([knopka_prozhanije_1], ))
        form_container_28 = flet.Container(width=280, height=400, top=275, left=15,
                                           content=flet.Column([knopka_prozhanije_2], ))
        form_container_29 = flet.Container(width=280, height=400, top=375, left=15,
                                           content=flet.Column([knopka_prozhanije_3], ))
        form_container_33 = flet.Container(width=280, height=400, top=475, left=15,
                                           content=flet.Column([knopka_prozhanije_4], ))
        form_container_30 = flet.Container(width=280, height=400, top=500, left=15,
                                           content=flet.Column([knopka_vyhod], ))
        form_container_31 = flet.Container(width=280, height=400, top=400, left=15,
                                           content=flet.Column([knopka_glavnaja_publikacija], ))
        form_container_32 = flet.Container(width=280, height=400, top=400, left=15,
                                           content=flet.Column([knopka_glavnaja_publikacija], ))


        uved=flet.SnackBar(flet.Text("Ввести новый платок", color=cvet_1, size=28,
                                                                     weight=flet.FontWeight.BOLD,
                                                                     font_family="Ponomar"), visible=True)
        uved_kont = flet.Container(width=1000, height=1000, top=0, left=0,content=flet.Column([uved]))
        #form_container_3 = flet.Container(width=280, height=600, top=900, left=495, content=flet.Column([otpravka_knopka],))
        #form_container_1 = flet.Container(width=275, height=900, top=50, left=215, content=flet.Column([
        #form_column_1=flet.Column([

        #form_container_2=flet.Container(width=280,height=600,top=100,left=495,content=flet.Column([

        #otpravka_knopka
    #],)
        form_container = flet.Container(width=275,height=250,top=190,left=400,content=flet.Column([
            flet.Text("Что надобно, мой Господин?", color=flet.Colors.DEEP_PURPLE,size=23, weight=flet.FontWeight.BOLD, font_family="Ponomar"),
            flet.TextField(label="Имя пользователя",color=flet.Colors.DEEP_PURPLE,label_style=flet.TextStyle(size=20,color=flet.Colors.DEEP_PURPLE),cursor_color=flet.Colors.DEEP_PURPLE, border_radius=10),
            flet.TextField(label="Электронная почта", color=flet.Colors.DEEP_PURPLE,label_style=flet.TextStyle(size=20,color=flet.Colors.DEEP_PURPLE),cursor_color=flet.Colors.DEEP_PURPLE, border_radius=10),
            flet.TextField(label="Пароль", color=flet.Colors.DEEP_PURPLE,label_style=flet.TextStyle(size=20,color=flet.Colors.DEEP_PURPLE), password=True, can_reveal_password=True, border_radius=10),
        ], tight=True
        ))
        #svjazka=flet.Container(content=flet.Row([form_column_1,form_column_2]))

        #page.background_color=flet.Colors(254,254,254)
        #РАЗНОЕ НАПОЛНЕНИЕ КНОПОК АДМИНА, ПРОДАВЦА, ТЕХНИКА И МАРКЕТОЛОГА
        from db_data_perfom import data_table2
        data_tablePROD=data_table2
        data_tableTehnik=data_table2
        data_tableMarket=data_table2
        #ТАБЛИЦА АДМИНА
        data_table2.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text("~")),flet.DataCell(knopka_bazadannyh_glavnaja),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")), ]))
        # В ХВОСТ ТАБЛИЦЫ ТЕХНИКА, ИМЕННО КНОПКИ ТЕХНИКА
        data_tableTehnik.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text("~")),flet.DataCell(knopka_tehnik_na_glavnuju),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")), ]))
        # В ХВОСТ ТАБЛИЦУ ПРОДАВЦА, ИМЕННО КНОПКИ ПРОДАВЦА
        data_tablePROD.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text("~")),flet.DataCell(knopka_prodavec_na_glavnuju),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")), ]))
        # В ХВОСТ ТАБЛИЦУ МАРКЕТОЛОГА, ИМЕННО КНОПКИ МАРКЕТОЛОГА
        data_tableMarket.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text("~")), flet.DataCell(knopka_marketolog_na_glavnuju),
        flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")), ]))
        from db_data_perfom import data_table2
        data_table2PROD = data_table2
        data_table2Tehnik = data_table2
        data_table2Market = data_table2
        data_table2.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text("~")),flet.DataCell(knopka_bazadannyh_glavnaja),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
                                                    flet.DataCell(flet.Text("~")), ]))
        data_table2PROD.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text("~")),flet.DataCell(knopka_prodavec_na_glavnuju),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),
                                                        flet.DataCell(flet.Text("~")), ]))
        data_table2Tehnik.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text("~")), flet.DataCell(knopka_tehnik_na_glavnuju),
        flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")), ]))
        data_table2Market.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text("~")), flet.DataCell(knopka_marketolog_na_glavnuju),
        flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")), ]))
        from db_data_perfom import data_table3
        data_table3PROD = data_table3
        data_table3Tehnik = data_table3
        data_table3Market = data_table3
        data_table3.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text("~")),flet.DataCell(knopka_bazadannyh_glavnaja),
        flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")), ]))
        data_table3PROD.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text("~")), flet.DataCell(knopka_prodavec_na_glavnuju),
        flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")), ]))
        data_table3Tehnik.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text("~")), flet.DataCell(knopka_tehnik_na_glavnuju),
        flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")), ]))
        data_table3Market.rows.append(flet.DataRow(cells=[flet.DataCell(flet.Text("~")), flet.DataCell(knopka_marketolog_na_glavnuju),
        flet.DataCell(flet.Text("~")), flet.DataCell(flet.Text("~")),flet.DataCell(flet.Text("~")),
        flet.DataCell(flet.Text("~")), ]))
        #ТАБЛИЦА С ПРОКРУТКОЙ ПО ПОГИЗОНТАЛИ И ВЕРТИКАЛИ
        table_container = flet.Column(controls=[flet.Row(controls=[data_table2], scroll=flet.ScrollMode.ALWAYS)],
                                  expand=True, scroll=flet.ScrollMode.ALWAYS)
        table_container2 = flet.Column(controls=[flet.Row(controls=[data_table2], scroll=flet.ScrollMode.ALWAYS)],
                                      expand=True, scroll=flet.ScrollMode.ALWAYS)
        table_container3 = flet.Column(controls=[flet.Row(controls=[data_table3], scroll=flet.ScrollMode.ALWAYS)],
                                       expand=True, scroll=flet.ScrollMode.ALWAYS)
        table_containerPR = flet.Column(controls=[flet.Row(controls=[data_tablePROD], scroll=flet.ScrollMode.ALWAYS)],
                                      expand=True, scroll=flet.ScrollMode.ALWAYS)
        table_containerPR2 = flet.Column(controls=[flet.Row(controls=[data_table2PROD], scroll=flet.ScrollMode.ALWAYS)],
                                       expand=True, scroll=flet.ScrollMode.ALWAYS)
        table_containerPR3 = flet.Column(controls=[flet.Row(controls=[data_table3PROD], scroll=flet.ScrollMode.ALWAYS)],
                                       expand=True, scroll=flet.ScrollMode.ALWAYS)
        table_containerTH = flet.Column(controls=[flet.Row(controls=[data_tableTehnik], scroll=flet.ScrollMode.ALWAYS)],
                                      expand=True, scroll=flet.ScrollMode.ALWAYS)
        table_containerTH2 = flet.Column(controls=[flet.Row(controls=[data_table2Tehnik], scroll=flet.ScrollMode.ALWAYS)],
                                       expand=True, scroll=flet.ScrollMode.ALWAYS)
        table_containerTH3 = flet.Column(controls=[flet.Row(controls=[data_table3Tehnik], scroll=flet.ScrollMode.ALWAYS)],
                                       expand=True, scroll=flet.ScrollMode.ALWAYS)
        table_containerMK = flet.Column(controls=[flet.Row(controls=[data_tableMarket], scroll=flet.ScrollMode.ALWAYS)],
                                        expand=True, scroll=flet.ScrollMode.ALWAYS)
        table_containerMK2 = flet.Column(controls=[flet.Row(controls=[data_table2Market], scroll=flet.ScrollMode.ALWAYS)],
                                         expand=True, scroll=flet.ScrollMode.ALWAYS)
        table_containerMK3 = flet.Column(controls=[flet.Row(controls=[data_table3Market], scroll=flet.ScrollMode.ALWAYS)],
                                         expand=True, scroll=flet.ScrollMode.ALWAYS)
        form_container_19 = flet.Container(top=20, left=1,
                                       content=flet.Column(controls=[table_container]))
        content_pirog_4 = flet.Stack([form_container_14,table_container
                               ])
        content_pirog_7 = flet.Stack([form_container_14, table_container2
                                      ])
        content_pirog_8 = flet.Stack([form_container_14, table_container3
                                      ])

        #ФОНОВЫЕ ПОДЛОЖКИ
        image_side = flet.Image(src=f"carica2.jpg", width=1050, height=1100)
        image_side_3 = flet.Image(src=f"carica5.jpg", width=1050, height=1100)
        image_side_2 = flet.Image(src=f"carica3.jpg", width=590, height=700)
        image_side_6 = flet.Image(src=f"carica-6.jpg", width=703, height=1000)
        image_side_7 = flet.Image(src=f"carica-7.jpg", width=590, height=900)
        image_side_8 = flet.Image(src=f"carica-8.jpg", width=590, height=900)
        #image_side=flet.Image(src=f"gamajun.jpg", width=320, height=500)
        content_pirog=flet.Stack([image_side,form_container_1,form_container_2,form_container_3,
                              form_container_4,form_container_5,form_container_6,form_container_7,form_container_8,form_container_9,form_container_15
                              #uved_kont
                              ])
        content_pirog_3=flet.Stack([image_side_3,form_container_10,form_container_11,form_container_13,form_container_4,form_container_5,
                                form_container_12,form_container_9,form_container_6,form_container_14
                                ])
        content_pirog_2 = flet.Stack([image_side_2,form_container_16,form_container_17,form_container_18,form_container_24, form_container_25,form_container_26
                                # uved_kont
                                ])
        #content_pirog_4 = flet.Stack([form_container_14,table_container
        #                           ])
        content_pirog_9 = flet.Stack(
            [image_side_6, form_container_27, form_container_28, form_container_29,form_container_33
             ])
        content_pirog_10 = flet.Stack(
            [image_side_7, form_container_30, form_container_31
             ])
        content_prodavec = flet.Stack(
            [image_side_7, container_kniga_posezhenija_PR,container_knopka_bazzadannyh_PR,container_knopka_zurnalpos_PR
             ])
        content_tehnik = flet.Stack(
            [image_side_8, container_kniga_posezhenija_TH, container_knopka_bazzadannyh_TH,
             container_knopka_zurnalpos_TH
             ])
        content_market = flet.Stack(
            [image_side_7, container_kniga_posezhenija_MK, container_knopka_bazzadannyh_MK,
             container_knopka_zurnalpos_MK
             ])
        knopka_vhod = flet.FilledButton("ВОЙТИ", width=200, height=40,
                                                   on_click=validate_user,
                                                   disabled=True, visible=True,
                                                   style=flet.ButtonStyle(color=flet.Colors.WHITE,
                                                                          bgcolor=flet.Colors.RED_500))
        knopka_oshibki_vhoda = flet.FilledButton("ОШИБКА ВХОДА:ВВЕДЕНЫ НЕКОРРЕКТНЫЕ ДАННЫЕ", width=335, height=50,
                                    on_click=validate_user,
                                    disabled=True, visible=False,
                                    style=flet.ButtonStyle(color=flet.Colors.WHITE,
                                                           bgcolor=flet.Colors.RED_500))
        form_container_19 = flet.Container(width=335, height=50, top=570, left=0,
                                       content=flet.Column([knopka_oshibki_vhoda], ))
        #page.add(flet.Column([#image_side,
        #data_table,
        #form_side
        #content_pirog_2],
        #scroll=flet.ScrollMode.AUTO
    #))
    #page.add(content_pirog_3)
        imja_polzovatelja=flet.TextField(label="Имя пользователя",border_radius=10,on_blur=vhod_validator)
        parol_polzovatelja=flet.TextField(label="Пароль",password=True,can_reveal_password=True,border_radius=10,on_blur=vhod_validator)
        form_side=flet.Container(top=575,height=200,content=flet.Column(controls=[flet.Text("Что надобно, мой Господин?",size=28,weight=flet.FontWeight.BOLD,font_family="Ponomar"),
        imja_polzovatelja,parol_polzovatelja,
        # flet.TextField(label="Э=лектронная почта",border_radius=10),
                                                           knopka_vhod],
                                                 horizontal_alignment=flet.CrossAxisAlignment.CENTER
        ))
        image_side_0=flet.Image(src=f"gamajun.jpg", width=360, height=800)
        content_pirog_4=flet.Stack([image_side_0,form_side,form_container_19])
        page.add(flet.Column([content_pirog_4],))
        # scroll=flet.ScrollMode.AUTO
        content_pirog_5=flet.Stack([image_side_4,form_container_20])
if __name__ == "__main__":
    flet.app(target=main,view=flet.AppView.WEB_BROWSER)

         #view=flet.AppView.WEB_BROWSER
