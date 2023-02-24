import streamlit as st
import pandas as pd
from io import StringIO


t1,t2,t3,t4 = st.tabs(['Home','แนะนำ','ดาวน์โหลด','ราคา'])
with t1:
    st.title('ต้นกระบองเพชรที่น่านำมาเลี้ยง')
    st.image('https://www.midori-garden.com/wp-content/uploads/2021/04/o95c2cd4b2efdd857fcd5d7818ebdd1bb_4620693218574021025_210315_59-1-1024x768.jpg')

with t2:
    menu_data = {
        "ต้นกระบองเพชรอิชินอปซิส": {"ต้นเตี้ย": True, "ต้นสูง": False, "ทนแดด": True,"รดน้ำน้อย": True, "รดน้ำเยอะ": False, "ขนหนา": False,"ขนบาง": True},

        "ต้นกระบองเพชรริบูเทีย พูลวิโนชา":  {"ต้นเตี้ย": True, "ต้นสูง": False, "ทนแดด": True,"รดน้ำน้อย": True, "รดน้ำเยอะ": False, "ขนหนา": True,"ขนบาง": False},

        "ต้นกระบอกเพชร ตุ๊กตาญี่ปุ่น":  {"ต้นเตี้ย": True, "ต้นสูง": False, "ทนแดด": True,"รดน้ำน้อย": True, "รดน้ำเยอะ": False, "ขนหนา": True,"ขนบาง": False},

        "ต้นกระบองเพชรม้าเวียน":  {"ต้นเตี้ย": True, "ต้นสูง": False, "ทนแดด": True,"รดน้ำน้อย": True, "รดน้ำเยอะ": False, "ขนหนา": False,"ขนบาง": True},

        "ต้นกระบองเพชรกุหลาบหิน":  {"ต้นเตี้ย": True, "ต้นสูง": False, "ทนแดด": False,"รดน้ำน้อย": False, "รดน้ำเยอะ": True, "ขนหนา": False,"ขนบาง": True},

        "ต้นกระบองเพชรคอนโดนางฟ้าหรือปราสาทนางฟ้า":  {"ต้นเตี้ย": False, "ต้นสูง": True, "ทนแดด": True,"รดน้ำน้อย": True, "รดน้ำเยอะ": False, "ขนหนา": False,"ขนบาง": True},

        "ต้นกระบองเพชรเสมา":  {"ต้นเตี้ย": False, "ต้นสูง": True, "ทนแดด": True,"รดน้ำน้อย": True, "รดน้ำเยอะ": False, "ขนหนา": False,"ขนบาง": True},

        "ต้นกระบองเพชรม้าลายโดนัท": {"ต้นเตี้ย": False, "ต้นสูง": True, "ทนแดด": False,"รดน้ำน้อย": True, "รดน้ำเยอะ": False, "ขนหนา": False,"ขนบาง": True},

        "ต้นกระบองเพชรว่านงาช้าง":  {"ต้นเตี้ย": False, "ต้นสูง": True, "ทนแดด": False,"รดน้ำน้อย": False, "รดน้ำเยอะ": True, "ขนหนา": False,"ขนบาง": True},

        "ต้นกระบองเพชรหยดน้ำ":  {"ต้นเตี้ย": True, "ต้นสูง": False, "ทนแดด": True,"รดน้ำน้อย": False, "รดน้ำเยอะ": True, "ขนหนา": False,"ขนบาง": True},

        "ต้นกระบองเพชรขนนกหรือแมมขนนก":  {"ต้นเตี้ย": True, "ต้นสูง": False, "ทนแดด": True,"รดน้ำน้อย": True, "รดน้ำเยอะ": False, "ขนหนา": True,"ขนบาง": False},

        "ต้นกระบองเพชรไมริโอ้หรือหมวกสังฆราช":  {"ต้นเตี้ย": True, "ต้นสูง": False, "ทนแดด": True,"รดน้ำน้อย": True, "รดน้ำเยอะ": False, "ขนหนา": False,"ขนบาง": True},
    }

    def display_menu_results(results):
        st.write("กระบองเพชรที่คูณอาจจะชอบ")
        for menu, prob in results.items():
            st.write(f"- {menu}: {prob:.2f}")

    st.title("คุณชอบกระบองเพขรแบบไหน?")
    st.write("โปรดเลือกลักษณะที่คุณชอบ เดี๋ยวทางเราจะทำการเลือกให้")
    st.write("ต้นทั่วไป = 0.8")
    st.write("ต้นที่แนะนำ = 0.12")

    # สร้างลักษณะ
    selected_characteristics = {}
    for characteristic in ["ต้นเตี้ย", "ต้นสูง", "ทนแดด", "รดน้ำน้อย", "รดน้ำเยอะ", "ขนหนา", "ขนบาง"]:
        selected_characteristics[characteristic] = st.checkbox(characteristic)

    # ทำนาย
    results = {}
    for menu, characteristics in menu_data.items():
        match = True
        for characteristic, selected in selected_characteristics.items():
            if selected and not characteristics[characteristic]:
                match = False
                break
            if match:
                results[menu] = 1.0

    if results:
        total_prob = sum(results.values())
        for menu, prob in results.items():
            display_menu_results({menu: prob / total_prob})
    else:
        st.write("ไม่พบที่ตรงกับลักษณะที่เลือก")

with t3:
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)

with t4:
    st.title('ราคาต้นกระบองเพชร')

        # อ่านข้อมูลจากไฟล์ Excel
    df = pd.read_excel('price.xlsx')
    avg_price = df['price'].mean()
    ava_price = df['price'].sum()

    st.write(df)
    st.write(f"ถ้าซื้อทั้งหมดราคา : {ava_price} บาท")
    st.write(f"ถ้าซื้อทั้งหมดราคาเฉลี่ยต้นละ : {avg_price:.2f} บาท")

st.sidebar.header('เลือกหมวดหมู่')
a1 = st.sidebar.button('ประเภทกระบองเพชร')
a2 = st.sidebar.button('การดูแลรักษา')
a3 = st.sidebar.button('คลิปที่เกี่ยวข้อง')

if a1:
    st.header("ต้นกระบองเพชรยอดฮิต 12 ชนิด")
    st.image('https://shopee.co.th/blog/wp-content/uploads/2020/06/%E0%B9%81%E0%B8%84%E0%B8%84%E0%B8%95%E0%B8%B1%E0%B8%AA.jpg')

    st.subheader('1.ต้นกระบองเพชรอิชินอปซิส')
    st.image('https://th.bing.com/th/id/R.23495900b596ac6b3e623a02d4867d92?rik=K3Ja5DRng6cRgg&pid=ImgRaw&r=0')
    st.write('☻ ชื่อภาษาอังกฤษ Echinopsis')
    st.write('☻ ชื่อทางวิทยาศาสตร์ Echinopsis sp')
    st.write('🌵จุดเด่นของต้นกระบองเพชรอิชินอปซิส🌵')
    st.write('- เป็นต้นกระบองเพชรที่มีหนามฟูๆสานอยู่รอบลำต้นแต่เป็นหนามอ่อน ไม่แหลมคม')
    st.write('- ออกดอกเป็นสีขาวหรือสีชมพูตามแต่สายพันธุ์ กลีบดอกมีลักษณะซ้อนกันเป็นชั้นๆ')
    st.write('- ก้านดอกมีความยาวและบานเฉพาะเวลากลางคืน')

    st.subheader('2.ต้นกระบองเพชรริบูเทีย พูลวิโนชา ')
    st.image('https://i.pinimg.com/originals/a0/65/06/a0650614107c94ebe776d702e5be1be9.png')
    st.write('☻ ชื่อภาษาอังกฤษ Rebutia pulvinosa')
    st.write('☻ ชื่อทางวิทยาศาสตร์ Rebutia pulvinosa F. Ritter & Buining')
    st.write('🌵จุดเด่นของต้นกระบองเพชรริบูเทีย🌵')
    st.write('- เป็นต้นกระบองเพชรที่มีไม่มีการแตกพูอย่างชัดเจน')
    st.write('- มีหนามสีขาวขึ้นรอบลำต้น แต่ค่อนข้างเปราะ')
    st.write('- มีดอทกระจายทั่วลำต้น')
    st.write('- ออกดอกแบบเดี่ยวบริเวณโคนต้น ให้ดอกหลายสีแต่กลีบดอกบาง')
    st.write('- ออกดอกในฤดูร้อน')
    st.write('- ริบูเทียออกผลที่มีลักษณะเป็นเมล็ดเล็กๆสีดำ')

    st.subheader('3.ต้นกระบอกเพชร ตุ๊กตาญี่ปุ่น ')
    st.image('https://cf.shopee.co.th/file/57dbff894b58771c7d93e479d13822f4_tn')
    st.write('☻ ชื่อภาษาอังกฤษ Mammillaria')
    st.write('☻ ชื่อทางวิทยาศาสตร์ Mammillaria gracilis Pfeiff.Ritter & Buining')
    st.write('🌵จุดเด่นของต้นกระบองเพชรตุ๊กตาญี่ปุ่น🌵')
    st.write('- เป็นต้นกระบองเพชรที่มีลำต้นทรงกลมแต่ออกยาวนิดหน่อย')
    st.write('- สีของลำต้นของตุ๊กตาญี่ปุ่นคือสีเขียวอ่อน')
    st.write('- ปกติแล้วหนามของตุ๊กตาญี่ปุ่นจะมีสีขาวแต่ถ้าเป็นหนามที่เพิ่งเกิดใหม่จะมีสีดำ')
    st.write('- เป็นกระบองเพชรพันธ์ุที่หนามเยอะมาก!! แน่นมาก')
    st.write('- ออกดอกหน้าหนาว')

    st.subheader('4.ต้นกระบองเพชรม้าเวียน ')
    st.image('https://th.bing.com/th/id/R.05c557f89299041793d61fd8476be363?rik=HG%2fTW8jqYwSNYw&pid=ImgRaw&r=0')
    st.write('☻ ชื่อภาษาอังกฤษ Haworthia limifolia')
    st.write('☻ ชื่อทางวิทยาศาสตร์ Haworthia limifolia Marloth')
    st.write('☻ ชื่อสามัญ File Leafed Haworthia, Fairies Washboard')
    st.write('🌵จุดเด่นของต้นกระบองเพชรม้าเวียน🌵')
    st.write('- เป็นต้นกระบองเพชรที่มีลำต้นเตี้ย ')
    st.write('- สามารถเกิดได้แบบต้นเดี่ยวและแดงกลุ่มเป็นกอ')
    st.write('- กระบอกเพชรม้าเวียนจะมีหน้าตาเหมือนใบที่เรียงเวียนรอบลำต้น')
    st.write('- มีร่องตรงระหว่างกลางและขอบตั้ง ปลายใบออกเรียวรีและแหลม มีลายนูนเป็นแนวขวาง')
    st.write('- ม้าเวียนมีสีเขียวเข้ม')
    st.write('- ออกดอกเป็นช่อ')
    st.write('- ออกดอกตลอดปีแต่จะออกเยอะที่สุดในหน้าร้อน')

    st.subheader('5.ต้นกระบองเพชรกุหลาบหิน ')
    st.image('https://www.cacpot.com/upload/activity/2020-07/21_1595174031.jpg')
    st.write('☻ ชื่อภาษาอังกฤษ Succulent plant')
    st.write('🌵จุดเด่นของกุหลาบหิน🌵')
    st.write('- เป็นไม้อวบน้ำที่ลำต้นดูอิ่มน้ำมาก น้องจะค่อนข้างอวบ')
    st.write('- ให้สัมผัสที่นุ่มนิ่ม เพราะในเนื้อเยื่อของกุหลาบหินประกอบด้วยน้ำเป็นจำนวนมาก')
    st.write('- ใบของกุหลาบกินจะมีความกลมและเป็นดอกซ้อนคล้ายๆดอกกุหลาบ')

    st.subheader('6.ต้นกระบองเพชรคอนโดนางฟ้าหรือปราสาทนางฟ้า ')
    st.image('https://th.bing.com/th/id/R.501c35ded65faef9125ea496f4090d38?rik=Wg0v95RWOSim%2fQ&riu=http%3a%2f%2fargyle-backpackers.com%2fwp-content%2fuploads%2f2020%2f09%2fIMG_2502-1024x682.jpg&ehk=uN0k8gyP58xXRBFh2uFipl6FN%2fd2JH9vJUhY3OXysik%3d&risl=&pid=ImgRaw&r=0')
    st.write('☻ ชื่อภาษาอังกฤษ Green finger')
    st.write('☻ ชื่อทางวิทยาศาสตร์ Acanthocereus tetragonus cv. Fairytale castle')
    st.write('🌵จุดเด่นของต้นกระบองเพชรคอนโดนางฟ้า🌵')
    st.write('- เป็นต้นกระบองเพชรที่มีลำต้นขนาดใหญ่ ตั้งตรงเหมือนกับปราสาทหรือจะเรียกแบบ2021 ก็คือคอนโด')
    st.write('- น้องมีลำต้นสีเขียว')
    st.write('- คอนโดนางฟ้าเป็นกระบองเพชรที่มีหนามแต่เป็นหนามสั้นและค่อนข้างเปราะ ')
    st.write('- หนามมีสีขาวและมีจำนวนมากในหนึ่งดอท')

    st.subheader('7.ต้นกระบองเพชรเสมา ')
    st.image('https://www.midori-garden.com/wp-content/uploads/2021/04/o95c2cd4b2efdd857fcd5d7818ebdd1bb_4620693218574021025_210315_42-768x576.jpg')
    st.write('☻ ชื่อภาษาอังกฤษ Prickly pear cactus')
    st.write('☻ ชื่อทางวิทยาศาสตร์ Nopalea cochenillifera (L.) Salm-Dyck')
    st.write('☻ ชื่อสามัญ Nopalea cochenillifera (L.) Salm-Dyck')
    st.write('🌵จุดเด่นของต้นกระบองเพชรเสมา🌵')
    st.write('- น้องคนนี้จุดเด่นอยู่ที่ลำต้นจะมีลักษณะแบนๆคล้ายใบเสมา')
    st.write('- มีหนามกระจายอยู่ตลอดลำต้นกระบองเพชร ')
    st.write('- แบ่งหนามของเสมาเป็น 2 ประเภท ได้แก่ หนามหลักที่มีความแข็ง และหนามตัวประกอบที่ค่อนข้างเปราะ')
    st.write('- หนามของน้องก่อให้เกิดความคัน ดังนั้นคนที่คิดจะเลี้ยงเสมาควรระมัดระวังเรื่องอาการแพ้')
    st.write('- ออกดอกหน้าหนาว ดอกเป็นสีแดงสวย')

    st.subheader('8.ต้นกระบองเพชรม้าลายโดนัท ')
    st.image('https://th.bing.com/th/id/R.61ebe41093618f6d282539f50c6dd252?rik=vloV9Cy05bOflQ&pid=ImgRaw&r=0')
    st.write('☻ ชื่อภาษาอังกฤษ The Zebra Plant')
    st.write('☻ ชื่อทางวิทยาศาสตร์ Haworthia fasciata (Willd.) Haw.')
    st.write('🌵จุดเด่นของต้นกระบองเพชรม้าลายโดนัท🌵')
    st.write('- เป็นไม้อวบน้ำลำต้นเตี้ย')
    st.write('- การโตเป็นแบบแผ่ออกด้านข้าง')
    st.write('- ใบน้องเป็นจำพวกใบเดี่ยว การเรียงเป็นแบบเวียน (คล้ายๆม้าเวียน)')
    st.write('- ใบมีลักษณะเป็นปลายแหลม มีสีขาวตัดตามแนวขวางของใบ จึงเรียกว่าม้าลาย')
    st.write('- ม้าลายโดนัทมีสีเขียวเข้ม')
    st.write('- ออกดอกเป็นช่อ')
    st.write('- ออกดอกตลอดปีแต่จะออกมาในหน้าร้อน')

    st.subheader('9.ต้นกระบองเพชรว่านงาช้าง ')
    st.image('https://img.biggo.com.tw/600,fit,subOeOLnWeTP6_DNuJevftZPCuD85NP8QGRIKovQ7Gn4/http://sub.tw/productimg/202006231630079fb3a5cc2391e5df2bbe68b1f92c0fa4.jpg')
    st.write('☻ ชื่อภาษาอังกฤษ Common Spear Plant')
    st.write('☻ ชื่อทางวิทยาศาสตร์ Sansevieria cylindrica Bojer ex Hook.')
    st.write('☻ ชื่อสามัญ Common Spear Plant, Spear Sansevieria')
    st.write('🌵จุดเด่นของต้นกระบองเพชรว่านงาช้าง🌵')
    st.write('- เป็นไม้พุ่ม ค่อนข้างสูง')
    st.write('- ลำต้นมีลักษณะเป็นเหง้าซ่อนอยู่ใต้ดิน')
    st.write('- ที่เห็นคือใบ (ลำต้นเทียม) ลักษณะเป็นทรงกระบอก ปลายแหลม')
    st.write('- น้องมีสีเขียวทั้งใบและจะมีลายสีเขียวเข้มในแนวขวาง')
    st.write('- ออกดอกเป็นช่อ มีความม้วนงอไปด้านหลัง ')
    st.write('- ดอกน้องเป็นสีขาวอมเหลือง')

    st.subheader('10.ต้นกระบองเพชรหยดน้ำ ')
    st.image('https://www.midori-garden.com/wp-content/uploads/2021/04/o95c2cd4b2efdd857fcd5d7818ebdd1bb_4620693218574021025_210315_18-600x450.jpg')
    st.write('☻ ชื่อภาษาอังกฤษ Haworthia cooperi')
    st.write('☻ ชื่อทางวิทยาศาสตร์ Haworthia cooperi var. truncata')
    st.write('☻ ชื่อสามัญ Haworthia cooperi var. truncata')
    st.write('🌵จุดเด่นของต้นกระบองเพชรหยดน้ำ🌵')
    st.write('- น้องมีใบที่ค่อนข้างสั้นและกลมบ๊อก')
    st.write('- ตรงส่วนปลายของใบจะมีความใสคล้ายๆหยดน้ำ จึงเป็นที่มาของชื่อหยดน้ำหรือหยดน้ำค้าง')
    st.write('- มีลักษณะขึ้นเป็นกอ')
    st.write('- น้องมีสีเขียว แต่เมื่ออายุมากขึ้นจะกลายเป็นสีเหลืองอมส้มหรือสีม่วง')
    st.write('- ไม่โตเร็วจนเกินไปแต่ก็ไม่โตช้าจนเจ้าของเครียด')
    st.write('- ปลูกง่าย เลี้ยงง่าย ไม่เรื่องมาก')

    st.subheader('11.ต้นกระบองเพชรขนนกหรือแมมขนนก ')
    st.image('https://www.midori-garden.com/wp-content/uploads/2021/04/image-111-768x494.jpeg')
    st.write('☻ ชื่อภาษาอังกฤษ Feather Cactus')
    st.write('☻ ชื่อทางวิทยาศาสตร์ Mammillaria plumosa F.A.C.Weber')
    st.write('🌵จุดเด่นของต้นกระบองเพชรขนนก🌵')
    st.write('- เป็นต้นกระบองเพชรที่มีลำต้นอวบน้ำ')
    st.write('- น้องเป็นกระบองเพชรต้นกลมบ๊อก แต่พูไม่ค่อยชัด')
    st.write('- มีหนามสีขาวคลุมลำต้น ดูสวยเบาคล้ายขนนก')
    st.write('- น้องมีดอกสีเดียวกับหนาม ในบางครั้งมีดอกสีชมพู')
    st.write('- ออกดอกในหน้าหนาว')

    st.subheader('12.ต้นกระบองเพชรไมริโอ้หรือหมวกสังฆราช ')
    st.image('https://th.bing.com/th/id/OIP.gVsjkdf9eTcOZkSm8_PmDAHaHa?pid=ImgDet&rs=1')
    st.write('☻ ชื่อภาษาอังกฤษ Bishop’s Cap, Deacons Hat, Miter Cactus')
    st.write('☻ ชื่อทางวิทยาศาสตร์ Astrophytum myriostigma Lem.')
    st.write('🌵จุดเด่นของต้นกระบองเพชรไมริโอ้🌵')
    st.write('- เป็นต้นกระบองเพชรที่ไม่ได้มีความคล้ายไมริโอ้ และคนก็มักเรียกผิดเนื่องจากชื่อคือ myrio')
    st.write('- น้องเป็นกระบองเพชรที่กลมบ๊อก')
    st.write('- ลำต้นมีสีเขียวอ่อนและมีพูชัดเจน')
    st.write('- มีหนามสีขาวเป็นกระจุกๆ และมีดอท')
    st.write('- ออกดอกแบบเดี่ยวและออกดอกที่ยอด ดอกมีลักษณะซ้อนกันเป็นชั้น สวยงามมาก')
    st.button("Home")

if a2:
    st.header('วิธีเลี้ยงต้นกระบองเพชรยอดฮิต 12 ชนิด')
    st.image('https://shopee.co.th/blog/wp-content/uploads/2020/06/cactusss-1140x800.jpg')
    st.subheader('ต้นกระบองเพชรอิชินอปซิส(Echinopsis)🌵')
    st.write('- สามารถเลี้ยงได้ในดินร่วน เพราะต้องการการระบายน้ำจากดินที่ค่อนข้างดี')
    st.write('- ไม่ค่อยต้องการน้ำ')
    st.write('- ต้องการแสงแดดจัด')

    st.subheader('ต้นกระบองเพชรริบูเทีย พูลวิโนชา (Rebutia pulvinosa F. Ritter & Buining)🌵')
    st.write('- สามารถเลี้ยงได้ในดินร่วนปนทราย')
    st.write('- ความต้องการน้ำอยู่ในเกณฑ์น้อยถึงปานกลาง')
    st.write('- ชอบแสงแดดจัด')
    st.write('- ทนแล้งได้ดีมาก')

    st.subheader('ต้นกระบอกเพชร ตุ๊กตาญี่ปุ่น (Mammillaria)🌵')
    st.write('- สามารถเลี้ยงได้ในดินร่วนปนทราย')
    st.write('- ความต้องการน้ำมีไม่มาก อยู่ในขั้นน้อยถึงกลางๆ')
    st.write('- ชอบแสงแดดค่อนข้างจัด')

    st.subheader('ต้นกระบองเพชรม้าเวียน (Haworthia limifolia)🌵')
    st.write('- สามารถเลี้ยงได้ในดินร่วนปนทราย')
    st.write('- ต้องการน้ำน้อย')
    st.write('- ชอบแสงแดดร่ม ไม่จัดมาก')
    st.write('- สามารถทนความแล้งได้เยี่ยม ')

    st.subheader('ต้นกระบองเพชรกุหลาบหิน (Succulent plant)🌵')
    st.write('- ต้องการแสงแดดค่อนข้างมาก แต่ชอบมากที่สุดคือแสงแดดในตอนที่อากาศค่อนข้างเย็น  ')
    st.write('- ชอบแสงแดดช่วงเช้า ไม่จัดมาก')
    st.write('- ไม่ค่อยชอบน้ำ')
    st.write('- หากต้องการรดน้ำควรทำในช่วงกลางคืน เพราะปากใบของกุหลาบหินจะทำงานเฉพาะเวลากลางคืน (สงสัยชอบทำโอ)')
    st.write('- ชอบอยู่ในที่เย็นและอากาศถ่ายเทสะดวก')

    st.subheader('ต้นกระบองเพชรคอนโดนางฟ้าหรือปราสาทนางฟ้า (Green finger)🌵')
    st.write('- สามารถเลี้ยงได้ในดินร่วนปนทราย ')
    st.write('- น้องคนนี้ต้องการน้ำปานกลาง')
    st.write('- ต้องการแสงแดดจัด')

    st.subheader('ต้นกระบองเพชรเสมา (Prickly pear cactus)🌵')
    st.write('- สามารถเลี้ยงได้ในดินร่วนปนทราย ที่ระบายน้ำได้ดี ขอย้ำว่าต้องระบายน้ำได้ดี')
    st.write('- ต้องการน้ำน้อย')
    st.write('- ชอบแดดจัดมาก')
    st.write('- ทนต่อความแล้ง')

    st.subheader('ต้นกระบองเพชรม้าลายโดนัท (The Zebra Plant)🌵')
    st.write('- สามารถเลี้ยงได้ในดินร่วนปนทราย ')
    st.write('- ต้องการน้ำปาน-น้อย')
    st.write('- น้องไม่ชอบแดดแรง น้องชอบแดดร่ม แบบแดดอ่อนๆรำไรๆ')
    st.write('- สามารถทนความแล้งได้ดี')

    st.subheader('ต้นกระบองเพชรว่านงาช้าง (Common Spear Plant)🌵')
    st.write('- ควรเลี้ยงในดินร่วนที่มีอินทรีย์วัตถุสูง')
    st.write('- ต้องการน้ำปานกลาง')
    st.write('- ชอบแสงแดดร่ม รำไรๆ')

    st.subheader('ต้นกระบองเพชรหยดน้ำ (Haworthia cooperi)🌵')
    st.write('- ชอบอากาศที่ถ่ายเท ปลอดโปร่ง')
    st.write('- ชอบดินที่ระบายน้ำได้ดี')
    st.write('- ชอบแสงแดดร่ม ไม่จัดมาก')
    st.write('- สามารถทนความแล้งได้เยี่ยม เพราะน้องอุ้มน้ำหนักมาก')

    st.subheader('ต้นกระบองเพชรขนนกหรือแมมขนนก (Feather Cactus)🌵')
    st.write('- สามารถเลี้ยงได้ในดินร่วนปนทราย ')
    st.write('- ต้องการน้ำน้อย-ปานกลาง')
    st.write('- ชอบแดดจัดๆๆๆขอแจ่มๆๆ')
    st.write('- ทนความแล้งได้เยี่ยม')

    st.subheader('ต้นกระบองเพชรไมริโอ้หรือหมวกสังฆราช (Bishop’s Cap)🌵')
    st.write('- สามารถเลี้ยงได้ในดินร่วนปนทราย ')
    st.write('- ต้องการน้ำปานกลาง')
    st.write('- ชอบแสงแดดจัดมาก')
    st.button("Home")

if a3:
    st.header('🌵คลิปที่เกี่ยวข้องกับกระบองเพชร🌵')
    st.subheader('Timelab cactus🌱')
    video1 = open('QQ.mp4', 'rb')
    video2 = video1.read()
    st.video(video2)

    st.subheader('HOW TO PROPAGATE CACTUS EASY & FAST')
    video1 = open('ZZ.mp4', 'rb')
    video2 = video1.read()
    st.video(video2)

    st.subheader('How and When to Water Succulents for Beginners💧🌱')
    video1 = open('WW.mp4', 'rb')
    video2 = video1.read()
    st.video(video2)
    st.button("Home")