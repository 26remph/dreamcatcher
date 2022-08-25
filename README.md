![(c) image load from tg-journal.com](https://tg-journal.com/wp-content/uploads/2021/04/illjuziya.jpg)
**DREAMCATCHER (Ловец сновидений)**

## Бот ловец сновидений 
Бот для записи сновидений в моменты пробуждения.
  
### О проекте
Мы знаем достаточно много о материи и ровным счетом ничего о природе самих себя.
Бот помогает картографировать ваши сны. Отлавливать и запоминать их. И лучше разобраться в том мире в котором вы проводите 1/3 своей жизни. 
В последствии, вы сможете сделать эти записи публичным и передать 
свой бесценный опыт.


### Как это работает
В момент пробуждения, когда ваши сны актуальны и ваше сознание ясно помнит контекст происходщего, вы записываете голосовое собщение с подробностями сна.
Отправляете боту. Бот переводит это в тектсовое сообщение и исходя из содержимого прикрепляет к заметке картинку. Так называемый маяк сновидения [3].
Картинка связывается с текстом сообщения и вашим голосовым сообщением. Каждый раз смотря на картинку вы сможете в точности воспроизвести в памяти все детали сна. Далее перечитав, вы вспомните дополнительные детали, о которых не подозревали. Дополняя вашу заметку новым текстом и маяками. Карта вашего сна станет намного детальней и отчетливей. Вы почувствуете себя магиланом в бескрайнем мире сознания.

[3] Методика запоминания огромных массивов данных по-средствам графиеческих образов.

####Бэклог проекта
- Дать возможность постить сновидения на сайт (/yatoube) 
- Использовать нейронную сеть для обучения и подбора картинок, которые наиболее точно соответствуют сновидению.
- Использовать нейросеть типа Nvida canvas, для преобразования каля-маля в хороший образ или отпечаток сновидения.
- Использовать нейронную сеть для классификации сновидения путешественника по известным классическим сонникам. 
(подобный алгоритму GPT-3)

### Авторы
Вадим Барсуков
... все желающие положить добротный проект в портфолио 
в качестве проекта для души
...

####Вместо заключения
Основные научные современные гипотезы[1] о происхождении жизни, так или иначе
утверждают что неживая материя из 6 компонентов (водород, кислород, углерод, азот, 
фосфор, сера) много миллионов лет назад, неким образом **самоорганизовалась** 
в РНК и таким же загадочным образом приобрела способность к репликации,
метаболизму и свойство изоляции от внешней среды. Путем неисчислимого цикла
обучения, трансформации генов мы имеем то что имеем. 
Мы научились разговаривать.

С другой стороны

С другой стороны есть не научный подход, теология и философия [2]
в основе которого лежит идея того что жизнь это проявление чего-то 
разумного "искры бога" в форме неживой материи.

Истина где-то рядом.

### Cсылки*

| сноска | ссылка                                      | описание                                                                       |
|--------|---------------------------------------------|--------------------------------------------------------------------------------|
| [1]    | https://www.mdpi.com/2075-1729/10/4/42/html | Defining Lyfe in the Universe: From Three Privileged Functions to Four Pillars |

(c) Part of project North Bridge Alavoine

[//]: # (![alternative header]&#40;https://img-fotki.yandex.ru/get/6427/130842948.2d6/0_15a026_d6b2f45e_XXXL.jpg&#41;)

### Технологии
- python 3.9
- python-telegram bot
- google serpapi
- google speech kit

####Техническое исполнение

Two handler function:
def write_text(update: Update, context: CallbackContext):
def say_voice(update: Update, context: CallbackContext):

...