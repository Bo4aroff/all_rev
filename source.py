from app_store_scraper import AppStore
from google_play_scraper import app, Sort, reviews_all
import uuid
import pandas as pd
import numpy as np
import plotly.express as px
import base64
from io import StringIO, BytesIO
import streamlit as st



        
def generate_excel_download_link(df_2):
    # Credit Excel: https://discuss.streamlit.io/t/how-to-add-a-download-excel-csv-function-to-a-button/4474/5
    towrite = BytesIO()
    df_selection.to_excel(towrite, encoding="utf-8", index=False, header=True)  # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="data_download.xlsx">Download Excel File</a>'
    return st.markdown(href, unsafe_allow_html=True)


#Мать и дитя
g_motherandchild = reviews_all(
        'ru.dmo.motherandchild',
        sleep_milliseconds=0,
        lang='ru',
        country='us',
        sort=Sort.NEWEST,
    )
g_df = pd.DataFrame(np.array(g_motherandchild),columns=['review'])
g_df2 = g_df.join(pd.DataFrame(g_df.pop('review').tolist()))

g_df2.drop(columns={'userImage', 'reviewCreatedVersion'},inplace = True, axis=1)
g_df2.rename(columns= {'score': 'rating','userName': 'user_name', 'reviewId': 'review_id', 'content': 'review_description', 'at': 'review_date', 'replyContent': 'developer_response', 'repliedAt': 'developer_response_date', 'thumbsUpCount': 'thumbs_up'},inplace = True)
g_df2.insert(loc=0, column='source', value='Google Play')
g_df2['Приложение'] = 'Мать и Дитя'
g_df2.insert(loc=3, column='review_title', value=None)


a_motherandchild = AppStore('ru', '1365552171')
a_motherandchild.review()


a_df = pd.DataFrame(np.array(a_motherandchild.reviews), columns=['review'])
a_df2_ = a_df.join(pd.DataFrame(a_df.pop('review').tolist()))

# a_df2_.drop(columns={'isEdited'},inplace = True, axis=1)
a_df2_.insert(loc=0, column='source', value='App Store')
a_df2_['Приложение'] = 'Мать и Дитя'
a_df2_['developer_response_date'] = None
a_df2_['thumbs_up'] = None
a_df2_.insert(loc=1, column='review_id', value=[uuid.uuid4() for _ in range(len(a_df2_.index))])
a_df2_.rename(columns= {'review': 'review_description','userName': 'user_name', 'date': 'review_date','title': 'review_title', 'developerResponse': 'developer_response'},inplace = True)
a_df2_ = a_df2_.where(pd.notnull(a_df2_), None)

#smartmed
g_smartmed = reviews_all(
        'ru.mts.smartmed',
        sleep_milliseconds=0,
        lang='ru',
        country='us',
        sort=Sort.NEWEST,
    )
g_df_ = pd.DataFrame(np.array(g_smartmed),columns=['review'])
g_df3 = g_df_.join(pd.DataFrame(g_df_.pop('review').tolist()))

g_df3.drop(columns={'userImage', 'reviewCreatedVersion'},inplace = True, axis=1)
g_df3.rename(columns= {'score': 'rating','userName': 'user_name', 'reviewId': 'review_id', 'content': 'review_description', 'at': 'review_date', 'replyContent': 'developer_response', 'repliedAt': 'developer_response_date', 'thumbsUpCount': 'thumbs_up'},inplace = True)
g_df3.insert(loc=0, column='source', value='Google Play')
g_df3['Приложение'] = 'SmartMed'
g_df3.insert(loc=3, column='review_title', value=None)


a_smartmed = AppStore('ru', '1348775741')
a_smartmed.review()


a_df_ = pd.DataFrame(np.array(a_smartmed.reviews), columns=['review'])
a_df3_ = a_df_.join(pd.DataFrame(a_df_.pop('review').tolist()))

# a_df3_.drop(columns={'isEdited'},inplace = True, axis=1)
a_df3_.insert(loc=0, column='source', value='App Store')
a_df3_['Приложение'] = 'SmartMed'
a_df3_['developer_response_date'] = None
a_df3_['thumbs_up'] = None
a_df3_.insert(loc=1, column='review_id', value=[uuid.uuid4() for _ in range(len(a_df3_.index))])
a_df3_.rename(columns= {'review': 'review_description','userName': 'user_name', 'date': 'review_date','title': 'review_title', 'developerResponse': 'developer_response'},inplace = True)
a_df3_ = a_df3_.where(pd.notnull(a_df3_), None)



#Доктор рядом
g_docnear = reviews_all(
        'ru.drclinics.app.docnear',
        sleep_milliseconds=0,
        lang='ru',
        country='us',
        sort=Sort.NEWEST,
    )
g_df_1 = pd.DataFrame(np.array(g_docnear),columns=['review'])
g_df4 = g_df_1.join(pd.DataFrame(g_df_1.pop('review').tolist()))

g_df4.drop(columns={'userImage', 'reviewCreatedVersion'},inplace = True, axis=1)
g_df4.rename(columns= {'score': 'rating','userName': 'user_name', 'reviewId': 'review_id', 'content': 'review_description', 'at': 'review_date', 'replyContent': 'developer_response', 'repliedAt': 'developer_response_date', 'thumbsUpCount': 'thumbs_up'},inplace = True)
g_df4.insert(loc=0, column='source', value='Google Play')
g_df4['Приложение'] = 'Доктор рядом'
g_df4.insert(loc=3, column='review_title', value=None)


a_docnear = AppStore('ru', '1185494141')
a_docnear.review()


a_df_1 = pd.DataFrame(np.array(a_docnear.reviews), columns=['review'])
a_df4_ = a_df_1.join(pd.DataFrame(a_df_1.pop('review').tolist()))

# a_df4_.drop(columns={'isEdited'},inplace = True, axis=1)
a_df4_.insert(loc=0, column='source', value='App Store')
a_df4_['Приложение'] = 'Неарклиник (Доктор рядом ios)'
a_df4_['developer_response_date'] = None
a_df4_['thumbs_up'] = None
a_df4_.insert(loc=1, column='review_id', value=[uuid.uuid4() for _ in range(len(a_df4_.index))])
a_df4_.rename(columns= {'review': 'review_description','userName': 'user_name', 'date': 'review_date','title': 'review_title', 'developerResponse': 'developer_response'},inplace = True)
a_df4_ = a_df4_.where(pd.notnull(a_df4_), None)

#Объеденил
a_df2 = pd.concat([g_df2,a_df2_, g_df3, a_df3_, g_df4, a_df4_])



a_df2['review_date'] = a_df2['review_date'].dt.strftime('%m/%d/%Y')
a_df2['date'] = pd.to_datetime(a_df2['review_date']).dt.floor('d')

a_df2['month'] = a_df2['date'].dt.month
a_df2['year'] = a_df2['date'].dt.year

a_df2.sort_values(by='review_date', inplace=True)

a_df2.loc[a_df2['rating'] < 4, 'рейтинг'] = 'Отрицательный'
a_df2.loc[a_df2['rating'] >= 4, 'рейтинг'] = 'Положительный'
a_df2.loc[a_df2['rating'] > 0, 'value'] = 1


st.set_page_config(page_title='Отзывы_SM', layout='wide')


year_options = a_df2['year'].unique().tolist()
month_options = a_df2['month'].unique().tolist()

st.sidebar.header('Фильтры:')

# year_ = st.sidebar.multiselect("Год", options=a_df2['year'].unique(), default=a_df2['year'].unique())
year_ = st.selectbox('ВЫБИРИТЕ ГОД', year_options, 0)
market = st.sidebar.multiselect("Ресурс", options=a_df2['source'].unique(), default=a_df2['source'].unique())
prog = st.sidebar.multiselect("Приложение", options=a_df2['Приложение'].unique(), default=a_df2['Приложение'].unique())
month_ = st.sidebar.multiselect("Месяц", options=a_df2['month'].unique(), default=a_df2['month'].unique())
raiting = st.sidebar.multiselect("Рейтинг", options=a_df2['рейтинг'].unique(), default=a_df2['рейтинг'].unique())


# month_ = st.slider("Month", max_value=max(a_df2['month'].unique().tolist()), min_value=min(a_df2['month'].unique().tolist()), value=(max(a_df2['month'].unique().tolist()), min(a_df2['month'].unique().tolist())))
df_selection = a_df2.query("рейтинг == @raiting & year == @year_ & month == @month_ & source == @market & Приложение == @prog")

st.title(":bar_chart: Основные показатели")
st.markdown('##')

average_raiting = round(df_selection['rating'].mean(), 1)
star_raiting = ":star:" * int(round(average_raiting, 0))


st.subheader("Средний Рейтинг:")
st.subheader(f"{average_raiting} {star_raiting}")

st.markdown("---")


# rating_by_value = (df_selection.groupby(by=['рейтинг']).sum()[['value']].sort_values(by="value"))
fig_rating = px.bar(df_selection,
                    x="value",
                    y='source',
                    orientation="h",
                    title="<b>Оценки</b>",
                    color='рейтинг',
                    color_discrete_map={
                "Отрицательный": "red",
                "Положительный": "green",},
                    )

st.plotly_chart(fig_rating)


fig_month = px.bar(df_selection,
                  x="month",
                  y="value",
                  orientation="v",
                  title="<b>Рейтинг за месяц</b>",
                  color="рейтинг",
                  color_discrete_map={
                "Отрицательный": "red",
                "Положительный": "green",},
                  )


st.plotly_chart(fig_month)

st.markdown("---")

# date_by_value = (df_selection.groupby(by=['date']).sum()[['value']].sort_values(by='date'))
fig_date = px.bar(df_selection,
                  x="date",
                  y="value",
                  orientation="v",
                  title="<b>Комментарии_(количество) по датам</b>",
                  color="рейтинг",
                  color_discrete_map={
                "Отрицательный": "red",
                "Положительный": "green",},

                  )


st.plotly_chart(fig_date)




# fig_new = px.bar(df_selection,
#                  x="рейтинг",
#                  y="value",
#                  title="<b>Динамика по дням</b>",
#                  color="рейтинг",
#                  animation_frame="review_date",
#                  animation_group="рейтинг",
#                 )
# fig_new.update_layout(width=800)
# st.write(fig_new)

if st.checkbox('Сформировать файл для скачивания'):

    df_2 = st.dataframe(df_selection)
if st.checkbox('Скачать файл Excel'):

    st.subheader('ССЫЛКА ДЛЯ СКАЧИВАНИЯ')
    generate_excel_download_link(df_2)
