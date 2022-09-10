# Ici on import les modules que nous avons besoin
from pytube import YouTube;
from print_color import print;
import os;

# On récupère l'URL de la vidéo par un input
yt = YouTube(str(input("Entez l'URL de la vidéo : ")));

video = yt.streams.filter(only_audio=True).first();

# On définit la destination de la vidéo de la ou on vont qu'il s'installe
destination = str("C:\\Users\\Name\\Music"); # Modifiez "Name" par votre nom d'utilisateur de votre PC

# On télécharge et prépare le fichier
out_file = video.download(output_path=destination);
base, ext = os.path.splitext(out_file);

# On demande le format de la vidéo que l'on souhaite
format = input('Entrez le format que vous voulez ! (mp3/mp4) ');

f = str(format);

thf = "";

# Ici on vérifie que le format donné est bien mp3 ou mp4
if f == "mp3" or f == ".mp3":
    thf = ".mp3";

    new_file = base + thf;

    os.rename(out_file, new_file);

    print(yt.title + " installé !", tag='SUCCES', tag_color='green', color='magenta')
elif f == "mp4" or f == ".mp4":
    thf = ".mp4";

    # On ajoute le format à fichier
    new_file = base + thf;

    # On renomme la vidéo installé avec le format choisi
    os.rename(out_file, new_file);

    print(yt.title + " installé !", tag='SUCCES', tag_color='green', color='magenta')
else:
    # Si le format donné n'est pas bon, alors le code enverra ce message d'erreur
    print('Le format doit être mp3 ou mp4 !', tag='ERROR', tag_color='red', color='magenta');
