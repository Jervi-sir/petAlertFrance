import pandas as pd
import json

# Read in the two CSV files
agr_df = pd.read_csv('aggregation_query.csv')
races_df = pd.read_csv('races.csv')

agr_df['animal.0.collar'] = agr_df['animal.0.collar'].fillna(99).replace(
  { 
    99: '', 'nan': 'null', 'unknown': 3,
    'Oui': 1, 'general_Yes': 1,
    'Non': 2, 'general_No': 2, 'No': 2
  }
)
agr_df['animal.0.collarType'] = agr_df['animal.0.collarType'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    'Nylon': 1, 'nylon': 1,
    'Plastique': 2, 'Plastic': 2, 'plástico': 2, 'plastique': 2,
    'chaîne': 3, 'Chaîne': 3, 'Chain': 3, 'Chaine': 3, 'Chainette': 3, 'chainette': 3, 'en chaînette': 3,
    'Cuir': 4, 'cuero': 4, 'Leather': 4, 'cuir': 4,
    'Corde': 5,
    'metálico': 6,
    'antipuces': 7, 'Anti puce': 7,
    'Tissus': 8, 'Tissu': 8,
    'Bleu': 9,
  }
)
agr_df['animal.0.collarKind'] = agr_df['animal.0.collarKind'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    '': '',
    'collar': 1, '\n collier ': 1,
    'harness': 2,  '\n harnais ': 2,
  }
)

agr_df['animal.0.collarColor'] = agr_df['animal.0.collarColor'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    'Beige': 1, 'beige': 1,
    'Black': 2, 'Noir': 2, 'noir et blanc': 2, 'noir': 2, 'negro': 2,
    'Blanc': 3, 'blanc': 3, 'blanco': 3, 'White': 3,
    'Bleu vert': 4, 'Bleu': 4, 'Blue': 4, 'bleu': 4, 'azul': 4,
    'Collier gps orange + collier rose': 5,
    'Green': 6,
    'Grey': 7, 'Gris': 7, 'gris': 7, 'grise': 7,
    'Jaune': 8, 'Yellow': 8, 'jaune fluo': 8, 'jaune': 8, 'amarillo': 8,
    'Kaki': 9, 'kaki': 9,
    'Marron': 10, 'Marron/beige': 10, 'marron': 10, 'Brown': 10,
    'ORANGE': 11, 'Orange Fluo': 11, 'Orange fluo': 11, 'Orange': 11, 'orange': 11,
    'Pink': 12, 'Rose': 12, 'rosa': 12, 'rose': 12,
    'Purple': 13, 'Violet': 13,
    'ROUGE': 14, 'Red': 14, 'Rouge avec boîtier noir': 14, 'Rouge': 14, 'rouge et noir': 14, 'rouge': 14,
    'VERT': 15, 'Vert': 15, 'verde': 15, 'vert fluorescent': 15, 'vert': 15,
  }
)

agr_df['animal.0.crossing'] = agr_df['animal.0.crossing'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    'unknown': 3,
    'Oui': 1,
    'Non': 2
  }
)

agr_df['animal.0.hair'] = agr_df['animal.0.hair'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    'sans': 0,
    'Court': 1, 'Courts': 1, 'courts': 1, 'Couts': 1, 'Courtsb': 1, 'corto': 1, 'Cou': 1, 'Shorthair': 1, 'court': 1,
    'Mi-longs': 2, 'mi-longs': 2, 'mi-long': 2, 'Mi-Longs': 2, 'mi-Longs': 2, 'Mi-long': 2, 'Mi- Longs': 2, 'mi longs': 2, 'Mi longs': 2,'Semi-longhair': 2, 'Semi-longs': 2, 'semilargo': 2,
    'long': 3, 'Longs': 3, 'Longhair': 3, 'Long': 3, 'largo': 3, 'longs': 3,
    'duro': 4, 'raides': 4, 'Dur': 4, 'Raides': 4, 'Stiff hair': 4,
    'rizado': 5, 'ras': 5, 'Ras': 5, 'Frisés': 5, 'frisés': 5, 'Curly hair': 5,
  }
)
agr_df['animal.0.mine'] = agr_df['animal.0.mine'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    True: 1,
    False: 2
  }
)
agr_df['animal.0.sex'] = agr_df['animal.0.sex'].fillna(99).replace(
  { 
    99: '', 'nan': 'null', 'unknown': 3,
    'Mâle': 1,
    'Femelle': 2,
  }
)
agr_df['animal.0.silhouette'] = agr_df['animal.0.silhouette'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    'Petite': 1, 'petite': 1,
    'Normale': 2, 'Normal': 2, 'normal': 2, 'normale': 2, 'Normales': 2,
    'Skinny': 3, 'maigre': 3, 'Maigre': 3, 'mince': 3, 'Mince': 3, 'Delgada': 3,
    'Moyenne': 4, 'Bien portant': 4,
    'Dodu': 5, 'dodue': 5, 'Plump': 5, 'Dodue': 5, 'gorda': 5,
    'No': 0, 'N': 0,
  }
)
agr_df['animal.0.size'] = agr_df['animal.0.size'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    'Small': 1, 'pequena': 1, 'petite': 1, 'petit': 1, 'Petite': 1, 'Petit': 1,
    'Medium': 2, 'mediana': 2, 'Moyen': 2, 'moyen': 2, 'moyenne': 2, 'Moyenne': 2,
    'Big': 3, 'Grande': 3, 'grand': 3, 'Grand': 3, 'grande': 3, 'dodue': 3,
    'Normal': 4,
  }
)
agr_df['animal.0.surgery'] = agr_df['animal.0.surgery'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    'unknown': 3,
    'Non': 2, 'No': 2,
    'Oui': 1, 'general_Yes': 1, 'Yes': 1,
  }
)
agr_df['animal.0.type'] = agr_df['animal.0.type'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    'Chat': 1, 
    'Chien': 2,
    'Autres': 3,
  }
)
agr_df['archive'] = agr_df['archive'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    True: 1
  }
)
agr_df['found'] = agr_df['found'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    False: 2,
    True: 1,
  }
)
agr_df['shareOnFb'] = agr_df['animal.0.surgery'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    False: 2,
    True: 1,
  }
)
agr_df['source'] = agr_df['source'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    'form': 1,
    'pawboost': 2,
    'bo': 3,
  }
)
agr_df['type'] = agr_df['type'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    'lost': 1,
    'found': 2,
    'saw': 3,
    'saw_dead': 4,
    'found_dead': 5,
    'dead': 6,
    'stolen': 7,
  }
)
agr_df['boFixed'] = agr_df['boFixed'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    False: 2,
    True: 1,
  }
)
agr_df['deleted'] = agr_df['deleted'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    True: 1,
   
  }
)
agr_df['fromEmail'] = agr_df['fromEmail'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    True: 1,
  }
)
agr_df['offerId'] = agr_df['offerId'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    '5b915527fb6fc02896196737': 1,
    '5b915589fb6fc028961967b6': 2
  }
)
agr_df['paid'] = agr_df['paid'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    False: 2,
    True: 1,
  }
)
agr_df['payment_status'] = agr_df['payment_status'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    'pending': 1,
    'done': 2,
  }
)
agr_df['animal.0.identified'] = agr_df['animal.0.identified'].fillna(99).replace(
  { 
    99: '', 'nan': 'null', 'unknown': 3,
    'Non': 2, 'no': 2,
    'Oui': 1, 'yes': 1,
  }
)
agr_df['animal.0.alive'] = agr_df['animal.0.alive'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    'Oui': 1,
    'Non': 2,
  }
)
agr_df['animal.0.source'] = agr_df['animal.0.source'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    'pawboost': 'pawboost'
  }
)
agr_df['source'] = agr_df['source'].fillna(99).replace(
  { 
    99: '', 'nan': 'null',
    'form': 1,
    'pawboost': 2,
    'bo': 3,
  }
)
agr_df['animal.0.tatouage'] = agr_df['animal.0.surgery'].fillna(99).replace(
  { 
    99: '', 'nan': 'null', 'unknown': 3,
    'Non': 2, 'No': 2, 'general_No': 2, 'N': 2,
    'Oui': 1, 'general_Yes': 1,
    'HCD 467': 1, '174 jyk': 1, '141SVG': 1, 'IE': 1, '132gbd': 1,
    'Oreille droite': 1, 'HJU641': 1, 'P': 1, 'HDC760': 1, '161UXX': 1, '132ayv': 1, '183TZB': 1,
    '2 BJT 648': 1, 'FDS605': 1, '166hln': 1, '146NHN': 1, '2GEX287': 1, '177SWJ': 1, '116NUT': 1,
    '189JCU': 1, 'Non tatouer': 1, '164TRU': 1, '159': 1, '187HZE': 1, '142ERU': 1, 'Croix': 1, 'JGX982': 1,
    'Hcw401': 1, 'JEK974': 1, '174TNZ': 1, 'JBP281': 1, 'P à l oreille d': 1, 'HLF875': 1, '190xnn': 1,
    '187XRL': 1, '160JLC': 1, '2gxm537': 1, 'HXF943': 1, 'Mal visible': 1, '167NGV': 1, '"S" oreille': 1,
    '119SAZ': 1, '175JBX': 1, 'FZR210': 1, 'DMN942': 1, 'FEL...': 1, 'Oreille gauche': 1,
    'IE illisible': 1, '189FHZ': 1, 'Pucee': 1,
  }
)

agr_df['boostId'] = agr_df['boostId'].fillna(99).replace(
  { 
    99: '', 'nan': 'null', 'unknown': 3,
    '5cc58fb99a00b30148045beb': 1,
    '5cc58fed9a00b30148045bec': 2,
    '5cc590019a00b30148045bed': 3,
  }
)

colors = { 
  99: '', 'nan': 'null', 'amarillo': 'null', 'Truite': 'null', 'purple': 'null',
  'Non renseignée': 0,
  'Azul merle': 1, 'Azul': 1, 'azul merle': 1, 'azul': 1,
  'Blanc': 2, 'Blanche': 2, 'blanco': 2, 'blanca': 2, 'blanc': 2, 'blanc et marron': 2, 'blanche': 2, 'noir et blanc': 2, 'Noir et blanc': 2, 'BLANC': 2, 'Tigre et blanc': 2, 'blanc et gris': 2, 'beige et blanc': 2, 'Blanco': 2, 'page_newpost_Chien_Mâle_Blanc': 2, 'Blanca': 2, 'Blanc et Noir': 2, 'marron et blanc': 2, 'Blanc et roux': 2, 'White': 2, 'white': 2, 'Blan': 2, 'Harlequin': 2, 'Isabelle': 2, 'harlequin': 2, 'isabelle': 2, 'angora Anglais': 2,
  'Bleu': 3, 'Bleu merle': 3, 'Bleue merle': 3, 'Bleue': 3, 'bleue': 3, 'bleu merle': 3, 'Blue merle': 3, 'Blue': 3, 'blue': 3,
  'Brindle': 4, 'Bringé': 4, 'Bringée': 4, 'Brun': 4, 'brindle': 4, 'bringé': 4, 'bringée': 4, 'brun': 4, 'brune': 4,
  'Calico': 5, 'Calicó Diluido': 5, 'Carey Diluido': 5, 'Carey': 5, 'Creme': 5, 'Crème / beige': 5, 'BEIGE': 5, 'Beige': 5, 'beige': 5, 'Diluted Calico': 5, 'Diluted Tortoiseshell': 5,
  'Ecaille de tortue': 6, 'Écaille de tortue': 6, 'ecaille de tortue': 6, 'écaille de tortue': 6, 'écaille de,tortue': 6,
  'FAUVE': 7, 'Fauve': 7, 'fauve': 7, 'Fuego': 7, 'fuego': 7,
  'Gris': 8, 'Grise': 8, 'gris': 8, 'grise': 8, 'page_newpost_Chien_Mâle_Gris': 8, 'Gris foncé': 8, 'Grey': 8, 'grey': 8,
  'Jaune': 9, 'jaune': 9, 'JAUNE': 9, 'Yellow': 9, 'yellow': 9,
  'Marron': 10, 'marron': 10, 'marron beige': 10, 'Marron clair': 10, 'Brown': 10, 'brown': 10, 'Marrón': 10, 'chocolat': 10, 'crème': 10, 'marrón': 10,
  'Merle': 11, 'arlequin': 11, 'atigrada': 11, 'atigrado': 11, 'Arlequin': 11, 'Atigrado': 11,
  'Naranja': 13, 'Ginger': 13, 'naranja': 13,
  'Noir': 14, 'Noire': 14, 'noir': 14, 'noire': 14, 'page_newpost_Chien_Femelle_Noir': 14, 'page_newpost_Chien_Mâle_Noir': 14, 'noir et fauve': 14, 'Black': 14, 'black': 14, 'Negra': 14, 'Negro': 14, 'Noi': 14, 'negra': 14, 'negro': 14,
  'Orange': 15, 'orange': 15,
  'Rose': 16, 'Pink': 16, 'Rosa': 16, 'Rosette': 16, 'Rousse foncée': 16, 'Rousse': 16, 'pink': 16, 'rosa': 16,
  'Rouge merle': 17, 'Rouge': 17, 'rouge merle': 17, 'rouge': 17, 'Red merle': 17, 'Red': 17, 'ROUX': 17, 'Roux': 17, 'Rojo merle': 17, 'Rojo': 17, 'page_newpost_Chat_Mâle_Roux': 17, 'red': 17, 'rojo merle': 17, 'rojo': 17, 'rousse': 17, 'roux': 17 ,
  'Sable': 18, 'sable': 18, 'Alezan': 18,
  'Tigré': 19, 'Tigre': 19, 'TIGRE': 19, 'tigrée grise': 19, 'Tigrée': 19, 'tigrée et blanche': 19, 'rayée': 19, 'tigré gris': 19, 'tigré marron': 19, 'Tigré gris': 19, 'tigré et blanc': 19, 'tigrée et blanche': 19, 'Tigré et blanc': 19, 'Tigrée et blanche': 19, 'blanche et tigrée': 19, 'blanc et tigré': 19, 'tabby': 19, 'ti': 19, 'tigre': 19, 'tigré': 19, 'tigrée': 19, 'tan': 19, 'Tabby': 19, 'Tan': 19, 'Tawny ': 19, 'Tawny': 19,
  'Tortoiseshell': 20, 'tortoiseshell': 20, 'calico': 20, 'carey': 20,
  'Tricolore dilué': 21, 'Tricolore diluée': 21, 'Tricolore diluée': 21, 'tricolore diluée': 21,
  'Tricolore': 22, 'Tricolor': 22, 'TRICOLORE': 22, 'omnicolore': 22, 'tricolor': 22, 'tricolore': 22,
  'Vert': 23, 'Verte': 23, 'vert': 23, 'verte': 23, 'Green': 23, 'green': 23, 'Verde': 23, 'verde': 23,
  'abigarrado': 24, 'Abigarrado': 24,
  'Écaille de tortue diluée': 25, 'Ecaille de tortue diluée': 25, 'ecaille de tortue diluée': 25, 'page_newpost_Chat_Femelle_Écaille de tortue diluée': 25, 'écaille de tortue dilué': 25, 'écaille de tortue diluée': 25,
}
agr_df['animal.0.color1'] = agr_df['animal.0.color1'].fillna(99).replace(colors)
agr_df['animal.0.color2'] = agr_df['animal.0.color2'].fillna(99).replace(colors)
agr_df['animal.0.color3'] = agr_df['animal.0.color3'].fillna(99).replace(colors)


agr_df['animal.0.race'] = agr_df['animal.0.race'].fillna(agr_df['animal.0.type_autres'])
agr_df['animal.0.race'] = agr_df['animal.0.race'].str.lower().str.replace(' ', '')
races_df['name_race'] = races_df['name_race'].str.lower().str.replace(' ', '')


merged_race_df = agr_df.merge(races_df, left_on='animal.0.race', right_on='name_race', how='left')
merged_race_df['animal.0.race'] = merged_race_df['id_race'].fillna(-1).astype(int).replace({-1: ''})
merged_race_df['animal.0.type'] = merged_race_df['especeId_race'].fillna(-1).astype(int).replace({-1: ''})

merged_race_df = merged_race_df.drop_duplicates(subset=['animal.0.collarColor', 'animal.0.name', 'animal.0.race', 'animal.0.sex', 'animal.0.type', 'message'], keep='first')
agr_df = agr_df.dropna(subset=['animal.0.photo'])

merged_race_df['id'] = range(1, len(merged_race_df) + 1)
merged_race_df = merged_race_df[['id'] + [col for col in merged_race_df.columns if col != 'id']]


def clean_string(s):
  list_data = json.loads(s)
  clean_s = ', '.join(list_data)
  return clean_s

#agr_df['animal.0.photo'] = agr_df['animal.0.photo'].apply(clean_string)


merged_race_df.rename(columns={'animal.0._id': 'animal._id'}, inplace=True)
merged_race_df.rename(columns={'animal.0.alive': 'animal.isAlive'}, inplace=True)
merged_race_df.rename(columns={'animal.0.collar': 'animal.hasCollar'}, inplace=True)
merged_race_df.rename(columns={'animal.0.collarColor': 'animal.collarColor'}, inplace=True)
merged_race_df.rename(columns={'animal.0.collarKind': 'animal.collarKind'}, inplace=True)
merged_race_df.rename(columns={'animal.0.collarType': 'animal.collarType'}, inplace=True)
merged_race_df.rename(columns={'animal.0.color1': 'animal.color1'}, inplace=True)
merged_race_df.rename(columns={'animal.0.color2': 'animal.color2'}, inplace=True)
merged_race_df.rename(columns={'animal.0.color3': 'animal.color3'}, inplace=True)
merged_race_df.rename(columns={'animal.0.crossing': 'animal.isCrossed'}, inplace=True)
merged_race_df.rename(columns={'animal.0.hair': 'animal.hair'}, inplace=True)
merged_race_df.rename(columns={'animal.0.mine': 'animal.isMine'}, inplace=True)
merged_race_df.rename(columns={'animal.0.identified': 'animal.isIdentified'}, inplace=True)
merged_race_df.rename(columns={'animal.0.name': 'animal.name'}, inplace=True)
merged_race_df.rename(columns={'animal.0.puce': 'animal.puce'}, inplace=True)
merged_race_df.rename(columns={'animal.0.race': 'animal.race'}, inplace=True)
merged_race_df.rename(columns={'animal.0.sex': 'animal.sex'}, inplace=True)
merged_race_df.rename(columns={'animal.0.silhouette': 'animal.silhouette'}, inplace=True)
merged_race_df.rename(columns={'animal.0.size': 'animal.size'}, inplace=True)
merged_race_df.rename(columns={'animal.0.surgery': 'animal.surgery'}, inplace=True)
merged_race_df.rename(columns={'animal.0.tatouage': 'animal.tatouage'}, inplace=True)
merged_race_df.rename(columns={'animal.0.type': 'animal.espece'}, inplace=True)
merged_race_df.rename(columns={'animal.0.type_autres': 'animal.type_autres'}, inplace=True)
merged_race_df.rename(columns={'animal.0.userId': 'animal.userId'}, inplace=True)
merged_race_df.rename(columns={'animal.0.userPseudo': 'animal.userPseudo'}, inplace=True)
merged_race_df.rename(columns={'animal.0.photo': 'animal.photo'}, inplace=True)
merged_race_df.rename(columns={'found': 'isFound'}, inplace=True)
merged_race_df.rename(columns={'paid': 'isPaid'}, inplace=True)
merged_race_df.rename(columns={'shareOnFb': 'isSharedOnFb'}, inplace=True)
merged_race_df.rename(columns={'type': 'Alert_type'}, inplace=True)
merged_race_df.rename(columns={'dpt': 'department'}, inplace=True)
merged_race_df.rename(columns={'deleted': 'isDeleted'}, inplace=True)
merged_race_df.rename(columns={'animal.0.birthday': 'animal.birthday'}, inplace=True)
merged_race_df.rename(columns={'animal.0.signes': 'animal.signes'}, inplace=True)
merged_race_df.rename(columns={'animal.0.source': 'animal.source'}, inplace=True)

merged_race_df = merged_race_df.reindex(columns=['id', 'Alert_type', 'department', 'boFixed', 'date', 'datePublished', 'dateCreated', 'message', 'postOnFb', 'boostDate', 'boostId', 'isPaid', 'payment_date', 'payment_status', 'address.formatted_address', 'address.city', 'country', 'coords.lat', 'coords.lng', 'contact.email', 'contact.facebook', 'contact.phone', 'archive', 'archiveDate', 'isFound', 'foundBy', 'foundDate', 'foundMessage', 'shareBy', 'shareDate', 'isSharedOnFb', 'takenBy', 'takenDate', 'isDeleted', 'deletedBy', 'deletedDate', 'source', 'statsView', 'fromEmail', 'messageFb', 'plannedDate', 'publifb_description', 'state', 'offerId', 'animal._id', 'animal.name', 'animal.photo', 'animal.sex', 'animal.espece', 'animal.race', 'animal.color1', 'animal.color2', 'animal.color3', 'animal.birthday', 'animal.isAlive', 'animal.isCrossed', 'animal.isMine', 'animal.isIdentified', 'animal.surgery', 'animal.puce', 'animal.hair', 'animal.signes', 'animal.silhouette', 'animal.size', 'animal.tatouage', 'animal.source', 'animal.hasCollar', 'animal.collarColor', 'animal.collarType', 'animal.collarKind', 'animalId', 'animal.userPseudo', 'animal.userId', 'userId', 'animal.type_autres', '_id', 'id_race', 'especeId_race', '_id_race', 'name_race'])

merged_race_df.to_csv('sanitized_no_duplicates.csv', index=False)


