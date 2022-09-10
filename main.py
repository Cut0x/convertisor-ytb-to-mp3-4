from pytube import YouTube;
from print_color import print;
import os;

yt = YouTube(str(input("Entez l'URL de la vidéo : ")));

video = yt.streams.filter(only_audio=True).first();

destination = str("C:\\Users\\Loïc\\Music\\Musique Download");

out_file = video.download(output_path=destination);
base, ext = os.path.splitext(out_file);

format = input('Entrez le format que vous voulez ! (mp3/mp4) ');

f = str(format);

thf = "";

if f == "mp3" or f == ".mp3":
    thf = ".mp3";

    new_file = base + thf;

    os.rename(out_file, new_file);

    print(yt.title + " installé !", tag='SUCCES', tag_color='green', color='magenta')
elif f == "mp4" or f == ".mp4":
    thf = ".mp4";

    new_file = base + thf;

    os.rename(out_file, new_file);

    print(yt.title + " installé !", tag='SUCCES', tag_color='green', color='magenta')
else:
    print('Le format doit être mp3 ou mp4 !', tag='ERROR', tag_color='red', color='magenta');
