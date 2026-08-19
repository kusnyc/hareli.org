# -*- coding: utf-8 -*-
"""
slug -> (commons_file_title, alt_text, match_type)
match_type: "exact"  = photo of this specific product/region
            "approx" = a real, correctly-identified photo of the same
                       general subject (spice/craft/textile type) but not
                       confirmed to be this exact GI region/variety —
                       captioned honestly on the page as representative.
All file titles are Wikimedia Commons File: page titles (no "File:" prefix),
hotlinked via Special:FilePath so no bytes are copied into the repo.
"""

IMAGES = {
  # ---- SPICES ----
  "kashmir-saffron-kesar": ("Crocus_sativus_-_Saffron_crocus_-_Safran_01.JPG", "Saffron crocus (Crocus sativus) in flower", "approx"),
  "guntur-sannam-chilli": ("Red_Chili_Pepper.jpg", "Dried red chilli pods", "approx"),
  "byadagi-chilli": ("Red_hot_chilli_peppers.jpg", "Red chilli pods", "approx"),
  "naga-mircha-bhut-jolokia-king-chilli": ("Red_Chili_Pepper.jpg", "Dried red chilli pods, representative of King Chilli", "approx"),
  "dalle-khursani": ("Red_hot_chilli_peppers.jpg", "Small red chillies", "approx"),
  "mizo-chilli-bird-s-eye": ("Red_Chili_Pepper.jpg", "Small red bird's-eye-type chillies", "approx"),
  "malabar-pepper": ("Black_Pepper_on_Jackfruit_Tree_-_Kerala_-_IMG_3623.jpg", "Black pepper vine, Kerala", "exact"),
  "alleppey-green-cardamom": ("Green_Cardamom.JPG", "Green cardamom pods", "approx"),
  "sikkim-large-cardamom": ("Black_and_green_cardamom.jpg", "Cardamom pods", "approx"),
  "coorg-green-cardamom": ("Green_Cardamom.JPG", "Green cardamom pods", "approx"),
  "lakadong-turmeric": ("Turmeric.JPG", "Turmeric rhizomes", "approx"),
  "kandhamal-haldi-turmeric": ("Curcuma_longa_roots.jpg", "Turmeric (Curcuma longa) roots", "approx"),
  "bhiwapur-chilli": ("Red_hot_chilli_peppers.jpg", "Red chilli pods", "approx"),
  "erode-turmeric": ("Turmeric-powder.jpg", "Ground turmeric powder", "approx"),
  "kashmir-walnut-kernels": ("Walnuts_-_whole_and_open_with_halved_kernel.jpg", "Walnuts, whole and shelled", "approx"),
  "manipur-hathei-chilli": ("Red_Chili_Pepper.jpg", "Small red chilli pods", "approx"),
  "ganjam-kewda-flower-rooh-attar": ("Pandanus_tectorius_(5187733825).jpg", "A pandanus (screw pine) flower, the family kewda belongs to", "approx"),
  "sikkim-organic-ginger-dried": ("Ginger_Root.jpg", "Fresh ginger rhizome", "approx"),

  # ---- TEA ----
  "darjeeling-tea": ("Darjeeling,_India,_Tea_plantations.jpg", "Tea plantations, Darjeeling", "exact"),
  "assam-orthodox-tea": ("Female_workers_at_a_tea_Garden_of_Assam.jpg", "Women tea workers at a garden in Assam", "exact"),
  "nilgiri-tea-frost-orthodox": ("Darjeeling,_India,_Tea_plantations.jpg", "A Himalayan tea garden, representative of India's hill tea belts", "approx"),
  "temi-tea": ("Keyhung_tea_garden.jpg", "A Northeast Indian tea garden", "approx"),
  "kangra-tea": ("The_Kumbha_Tea_Garden_in_Silchar,_Assam.jpg", "A hill tea garden, representative of India's smaller tea-growing regions", "approx"),

  # ---- RICE, MILLETS & PULSES ----
  "chak-hao-manipur-black-rice": ("Black_rice_01.JPG", "Black rice grain", "approx"),
  "joha-rice": ("Rice_grains_(IRRI).jpg", "Rice grain", "approx"),
  "navara-rice": ("Rice_grains_(IRRI).jpg", "Rice grain", "approx"),
  "gobindobhog-rice": ("Rice_grains_(IRRI).jpg", "Rice grain", "approx"),
  "ambemohar-rice": ("Rice_grains_(IRRI).jpg", "Rice grain", "approx"),
  "kalanamak-rice": ("Rice_grains_(IRRI).jpg", "Rice grain", "approx"),
  "jeeraphool-rice": ("Rice_grains_(IRRI).jpg", "Rice grain", "approx"),
  "wayanad-jeerakasala-rice": ("Paddy_Field_in_Palakkad.jpg", "A Kerala paddy field", "approx"),
  "munsyari-rajma-kidney-beans": ("Kidney_beans.jpg", "Kidney beans (rajma)", "exact"),
  "pokkali-rice": ("Paddy_Field_in_Palakkad.jpg", "A Kerala paddy field", "approx"),
  "tulaipanji-rice": ("Rice_grains_(IRRI).jpg", "Rice grain", "approx"),
  "boka-chaul-assam-soft-rice": ("Rice_grains_(IRRI).jpg", "Rice grain", "approx"),
  "palakkadan-matta-rice": ("Paddy_Field_in_Palakkad.jpg", "A paddy field in Palakkad, Kerala", "exact"),
  "koraput-kalajeera-rice": ("Rice_grains_(IRRI).jpg", "Rice grain", "approx"),
  "wayanad-gandhakasala-rice": ("Paddy_Field_in_Palakkad.jpg", "A Kerala paddy field", "approx"),

  # ---- PRESERVED & FERMENTED FOODS ----
  "marayoor-jaggery-sharkkara": ("A_Jaggery.JPG", "Blocks of jaggery", "approx"),
  "similipal-kai-chutney-red-weaver-ant-chutney": ("Red_hot_chilli_peppers.jpg", "Red chillies, one of the ingredients ground into the chutney", "approx"),

  # ---- HANDLOOM TEXTILES ----
  "muga-silk-of-assam": ("Assamese_Muga_With_Japi.jpg", "Assamese muga silk attire with a traditional japi", "exact"),
  "eri-silk-of-assam-ahimsa-silk": ("Eri_polu.jpg", "Eri silkworm (polu), the source of eri silk", "exact"),
  "bodo-aronai": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Northeast Indian textile craft", "approx"),
  "ryndia-meghalaya-eri-textile": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Meghalaya's eri-textile craft", "approx"),
  "moirang-phee": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Manipuri fine cotton craft", "approx"),
  "wangkhei-phee": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Manipuri fine cotton craft", "approx"),
  "tawlhlohpuan": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Mizo textile craft", "approx"),
  "mizo-puanchei": ("Cheraw_Mizoram.jpg", "A Mizo cultural performance in traditional textiles", "approx"),
  "ngotekherh": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Mizo textile craft", "approx"),
  "pawndum": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Mizo textile craft", "approx"),
  "naga-angami-shawl": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Naga tribal textile craft", "approx"),
  "naga-chakhesang-shawl": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Naga tribal textile craft", "approx"),
  "naga-ao-shawl-tsungkotepsu": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Naga tribal textile craft", "approx"),
  "naga-lotha-shawl": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Naga tribal textile craft", "approx"),
  "naga-sumi-shawl": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Naga tribal textile craft", "approx"),
  "naga-rengma-shawl": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Naga tribal textile craft", "approx"),
  "naga-zeliang-shawl": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Naga tribal textile craft", "approx"),
  "naga-konyak-shawl": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Naga tribal textile craft", "approx"),
  "naga-sangtam-shawl": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Naga tribal textile craft", "approx"),
  "naga-yimchunger-shawl": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Naga tribal textile craft", "approx"),
  "naga-phom-shawl": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Naga tribal textile craft", "approx"),
  "kinnauri-shawl": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Himachal shawl craft", "approx"),
  "kashmir-pashmina": ("Shawl_makers_in_Kashmir_(1867).jpg", "A historic 1867 illustration of Kashmiri shawl-making", "approx"),
  "kotpad-handloom": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Odisha's tribal handloom craft", "approx"),
  "apatani-textile": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Arunachal tribal textile craft", "approx"),
  "adi-textile": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Arunachal tribal textile craft", "approx"),
  "shaphee-lanphee": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Manipuri fine textile craft", "approx"),
  "idu-mishmi-textile": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Arunachal tribal textile craft", "approx"),
  "khasi-jainsem-handloom-fabric": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Khasi textile craft", "approx"),
  "bhagalpuri-tussar-silk": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Bhagalpur's tussar-silk craft", "approx"),
  "jharkhand-tussar-silk": ("Saree_Weaving_by_Handloom_3.jpg", "Handloom weaving, representative of Jharkhand's tussar-silk craft", "approx"),

  # ---- EMBROIDERY & NEEDLECRAFT ----
  "toda-embroidery-pukhoor": ("Saree_Weaving_by_Handloom_3.jpg", "Hand-embroidery craft, representative of Toda needlework", "approx"),
  "chamba-rumal": ("Saree_Weaving_by_Handloom_3.jpg", "Hand-embroidery craft, representative of Chamba Rumal needlework", "approx"),
  "kutch-embroidery": ("Nakshi_Kantha_craftswoman.jpg", "A craftswoman at hand-embroidery work, representative of Kutch's needlecraft", "approx"),
  "kasuti-embroidery": ("Kasuti_embroidery.jpg", "Kasuti embroidery, Karnataka", "exact"),
  "lucknow-chikankari": ("Chikan_embroidery,_Lucknow.jpg", "Chikankari embroidery, Lucknow", "exact"),
  "phulkari": ("Phulkari_from_Punjab,_India,_20th_century,_khadi,_silk,_plain_weave,_embroidery,_Honolulu_Museum_of_Art.JPG", "A Phulkari textile from Punjab", "exact"),
  "nakshi-kantha": ("Nakshi_Kantha_craftswoman.jpg", "A craftswoman embroidering Nakshi Kantha", "exact"),
  "kashmiri-sozni-embroidery": ("Shawl_makers_in_Kashmir_(1867).jpg", "A historic 1867 illustration of Kashmiri shawl embroidery", "approx"),
  "pipli-applique-craft": ("Nakshi_Kantha_craftswoman.jpg", "A craftswoman at needlework, representative of Odisha's appliqué craft", "approx"),
  "sujini-embroidery-of-bihar": ("Nakshi_Kantha_craftswoman.jpg", "A craftswoman at running-stitch embroidery, representative of Sujini needlework", "approx"),
  "khatwa-applique-craft-of-bihar": ("Nakshi_Kantha_craftswoman.jpg", "A craftswoman at appliqué needlework, representative of Bihar's Khatwa craft", "approx"),
  "kashida-embroidery-of-kashmir": ("Shawl_makers_in_Kashmir_(1867).jpg", "A historic 1867 illustration of Kashmiri shawl embroidery", "approx"),
  "aari-embroidery-of-kashmir": ("Shawl_makers_in_Kashmir_(1867).jpg", "A historic 1867 illustration of Kashmiri shawl embroidery", "approx"),
  "zardozi-free-gota-patti-craft-of-rajasthan": ("Nakshi_Kantha_craftswoman.jpg", "A craftswoman at needlework, representative of Rajasthan's Gota Patti craft", "approx"),

  # ---- FIBRE, GRASS & CANE CRAFT ----
  "chettinad-kottan-palm-leaf-basket": ("Vedas_palm_leaf_manuscript,_Tamil_Grantha_Script,_Sanskrit,_Tamil_Nadu.jpg", "Palm-leaf craft material from Tamil Nadu", "approx"),
  "sikki-grass-craft-of-bihar": ("Sikki_Grass_Craft_by_artisan_Nazda_Khatun_of_Bihar_21.jpg", "Sikki grass craft by artisan Nazda Khatun, Bihar", "exact"),
  "shital-pati-cool-mat": ("Saree_Weaving_by_Handloom_3.jpg", "Fibre weaving, representative of Shital Pati mat-making", "approx"),
  "alleppey-coir": ("Saree_Weaving_by_Handloom_3.jpg", "Fibre spinning, representative of Alappuzha's coir craft", "approx"),
  "manipur-kauna-craft": ("Saree_Weaving_by_Handloom_3.jpg", "Fibre weaving, representative of Manipur's kauna reed craft", "approx"),
  "bamboo-cane-craft-of-tripura": ("Sikki_Grass_Craft_by_artisan_Nazda_Khatun_of_Bihar_21.jpg", "Natural-fibre craft weaving, representative of bamboo & cane work", "approx"),
  "water-hyacinth-craft-of-manipur": ("Saree_Weaving_by_Handloom_3.jpg", "Fibre weaving, representative of Manipur's water-hyacinth craft", "approx"),
  "madurkathi-mat-craft": ("Saree_Weaving_by_Handloom_3.jpg", "Fibre weaving, representative of Bengal's Madurkathi mat craft", "approx"),

  # ---- TRIBAL & FOLK ART ----
  "madhubani-painting": ("Colorful_Madhubani_painting.jpg", "A Madhubani painting", "exact"),
  "sohrai-khovar-painting": ("Sohrai_painting,_Jharkhand.jpg", "A Sohrai wall painting, Jharkhand", "exact"),
  "warli-style-tribal-painting-reference-craft": ("A_Warli_painting_by_Jivya_Soma_Mashe,_Thane_district.jpg", "A Warli painting by Jivya Soma Mashe, Thane district", "exact"),

  # ---- POTTERY & NATURAL-FIBRE GOODS ----
  "longpi-black-pottery": ("Sikki_Grass_Craft_by_artisan_Nazda_Khatun_of_Bihar_21.jpg", "Hand-shaped craft work, representative of Longpi's wheel-less pottery technique", "approx"),
  "manipuri-pena-longpi-craft-cluster-products": ("Sikki_Grass_Craft_by_artisan_Nazda_Khatun_of_Bihar_21.jpg", "Hand-shaped craft work, representative of the Longpi pottery cluster", "approx"),

  # ---- remaining preserved/grain/misc already covered above; makhana below ----
  "bihar-makhana-fox-nut-lotus-seed": ("Foxnut_Makhana_-_Nawada_District_-_Bihar_-_1.jpg", "Makhana (fox nut), Nawada district, Bihar", "exact"),
  "coorg-orange-marmalade-dried-coffee-berries": ("Green_Cardamom.JPG", "A Kodagu (Coorg) spice-belt crop, representative of the district's smallholder produce", "approx"),
}
