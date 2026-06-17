import os
import json
import tempfile

config_path = os.path.join(tempfile.gettempdir(), "namazVaktiPro.json")

config = {
    "il": "İstanbul",
    "ilce": "İstanbul",
    "bildirim":True,
    "namazTrue":[
        {
            "ayetNo":"Bakara - 3",
            "ayet":"(Onlar) gayba iman ederler, namazı kılarlar, kendilerine verdiklerimizden hayra harcarlar"
        },
        {
            "ayetNo":"Nisa - 103",
            "ayet":"Namazı bitirince de ayakta iken, otururken ve yatarken Allah’ı anın. Güvenlik içinde olduğunuzda namazı gerektiği gibi kılın.\n\nŞüphe yok ki namaz, müminler üzerine vakitleri belli olarak yazılmış bir ödevdir"
        },
        {
            "ayetNo":"Mü'minun - 2",
            "ayet":"Ki onlar, namazlarında derin bir saygı hali yaşarlar"
        },
        {
            "ayetNo":"Mü'minun - 9",
            "ayet":"Namazlarını titizlikle eda ederler"
        },
        {
            "ayetNo":"Bakara - 153",
            "ayet":"Ey iman edenler! Sabır ve namazla yardım dileyin. Şüphesiz Allah sabredenlerin yanındadır"
        },
        {
            "ayetNo":"Hicr - 97",
            "ayet":"Andolsun, onların söyledikleri şeylerden dolayı göğsünün daraldığını biliyoruz"
        },
        {
            "ayetNo":"Bakara - 46",
            "ayet":"Onlar kesinlikle rablerine kavuşacaklarını ve O’na döneceklerini bilen kimselerdir"
        },
        {
            "ayetNo":"Bakara - 277",
            "ayet":"Şüphe yok ki iman edip dünya ve âhiret için yararlı şeyler yapanlar, namaz kılanlar ve zekât verenlerin rableri katında ecirleri vardır; onlara ne korku vardır ne de üzüleceklerdir"
        },
        {
            "ayetNo":"Taha - 14",
            "ayet":"Kuşkusuz ben, yalnız ben Allahım. Benden başka tanrı yoktur. O halde bana kulluk et, beni hatırında tutmak için namazı kıl”"
        },
        {
            "ayetNo":"Meryem - 55",
            "ayet":"Halkına namazı ve zekâtı emrederdi ve rabbinin rızâsına ermişti"
        }
    ],
    "namazFalse":[
        {
            "ayetNo":"Al'i - İmran",
            "ayet":"(Resulüm!) İnkâr edenlere de ki: Yakında mağlûp olacaksınız ve cehenneme sürükleneceksiniz. Orası ne kötü bir kalma yeri!"
        },
        {
            "ayetNo":"Maun - 4-7",
            "ayet":"Vay haline o namaz kılanların ki, Onlar namazlarının özünden uzaktırlar. Onlar halka gösteriş yaparlar. Hayra da engel olurlar."
        },
        {
            "ayetNo":"Müddessir - 42-43",
            "ayet":"“Sizi şu yakıcı ateşe sokan nedir?” Onlar şöyle cevap verirler: Biz namaz kılanlardan değildik"
        },
        {
            "ayetNo":"Meryem - 59",
            "ayet":"Sonra bunların ardından artık namazı kılmayan ve nefsânî arzulara uyan bir nesil geldi. Bunlar elbette azgınlıklarının cezasını bulacaklardır"
        },
        {
            "ayetNo":"Taha - 124",
            "ayet":"Kim de beni anmaktan yüz çevirirse mutlaka sıkıntılı bir hayatı olacaktır ve onu kıyamet günü kör olarak haşrederiz”"
        },
        {
            "ayetNo":"Mürselat - 48",
            "ayet":"Onlara, “Allah’ın huzurunda eğilin!” denildiğinde eğilmiyorlar"
        },
        {
            "ayetNo":"İbrahim - 3",
            "ayet":"Onlar, dünya hayatını âhirete tercih eden, Allah yolundan alıkoyan ve onu eğri göstermek isteyenlerdir; işte onlar derin bir sapkınlık içindedirler"
        }
    ]
}


def namazVaktiProConfig():
    
    if not os.path.exists(config_path):configDegistir()

    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def configDegistir(
    il="boş",
    ilce="boş",
    bildirim=False,
):

    if il == "boş":
        il = namazVaktiProConfig()["il"]
    if ilce == "boş":
        ilce = namazVaktiProConfig()["ilce"]
    
    config["il"] = il
    config["ilce"] = ilce
    config["bildirim"] = bildirim

    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=4)

if not os.path.exists(config_path):configDegistir("i̇stanbul","i̇stanbul")
