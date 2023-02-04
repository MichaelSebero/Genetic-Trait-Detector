filename = input("Enter the location of DNA data file: ")
# Bipolar Disorder
keyword1 = "rs1006737"
keyword2 = "A	A" or "A|A"
keyword3 = "rs4027132"
keyword4 = "A	A" or "A|A" or "A	G" or "A|G"
keyword5 = "rs7570682"
keyword6 = "A	A" or "A|A"
keyword7 = "rs1375144"
keyword8 = "C	C" or "C|C"
keyword9 = "rs683395"
keyword10 = "C	T" or "C|T"
keyword11 = "rs2609653"
keyword12 = "C	T" or "C|T" or "C	C" or "C|C"
keyword13 = "rs10982256"
keyword14 = "C	C" or "C|C"
keyword15 = "rs11622475"
keyword16 = "C	C" or "C|C"
keyword17 = "rs1344484"
keyword18 = "T	T" or "T|T"
keyword19 = "rs2953145"
keyword20 = "C	G" or "C|G" or "G	G" or "G|G"
keyword21 = "rs420259"
keyword22 = "T	T" or "T|T"
keyword23 = "rs4276227"
keyword24 = "C	C" or "C|C"
# Alzheimer's Disease
keyword25 = "rs429358"
keyword26 = "C	C" or "C|C" or "C	T" or "C|T"
keyword27 = "rs145999145"
keyword28 = "A	A" or "A|A" or "A	G" or "A|G"
keyword29 = "rs908832"
keyword30 = "A	A" or "A|A"
keyword31 = "rs63750847"
keyword32 = "A	A" or "A|A" or "A	G" or "A|G"
# Autism
keyword33 = "rs1858830"
keyword34 = "C	C" or "C|C" or "C	G" or "C|G"
keyword35 = "rs2710102"
keyword36 = "C	C" or "C|C" or "T	T" or "T|T"
keyword37 = "rs7794745"
keyword38 = "A	T" or "A|T" or "T	T" or "T|T"
keyword39 = "rs1322784"
keyword40 = "C	C" or "C|C" or "C	T" or "C|T" or "T	T" or "T|T"
keyword41 = "rs265981"
keyword42 = "A	G" or "A|G" or "G	G" or "G|G"
keyword43 = "rs4532"
keyword44 = "C	T" or "C|T" or "T	T" or "T|T"
keyword45 = "rs686"
keyword46 = "A	G" or "A|G" or "A	A" or "A|A"
keyword47 = "rs1143674"
keyword48 = "A	G" or "A|G" or "A	A" or "A|A"
keyword49 = "rs6807362"
keyword50 = "C	C" or "C|C"
keyword51 = "rs757972971"
keyword52 = "A	G" or "A|G" or "A	A" or "A|A"
keyword53 = "rs2217262"
keyword54 = "A	A" or "A|A"
keyword55 = "rs6766410"
keyword56 = "A	A" or "A|A" or "A	C" or "A|C" or "C	C" or "C|C"
keyword57 = "rs1445442"
keyword58 = "A	A" or "A|A" or "A	G" or "A|G" or "G	G" or "G|G"
keyword59 = "rs2421826"
keyword60 = "C	T" or "C|C" or "T	T" or "T|T" or "C	C" or "C|C"
keyword61 = "rs1358054"
keyword62 = "G	G" or "G|G" or "G	T" or "G|T" or "T	T" or "T|T"
keyword63 = "rs536861"
keyword64 = "A	A" or "A|A" or "A	C" or "A|C" or "C	C" or "C|C"
keyword65 = "rs722628"
keyword66 = "A	A" or "A|A" or "A	G" or "A|G" or "G	G" or "G|G"
# Schizophrenia
keyword67 = "rs27388"
keyword68 = "A	A" or "A|A" or "A	G" or "A|G"
keyword69 = "rs2270641"
keyword70 = "G	G" or "G|G"
keyword71 = "rs4129148"
keyword72 = "C	C" or "C|C" or "C	G" or "C|G"
keyword73 = "rs28694718"
keyword74 = "A	A" or "A|A" or "A	G" or "A|G"
keyword75 = "rs6422441"
keyword76 = "C	C" or "C|C" or "C	T" or "C|T"
keyword77 = "rs28414810"
keyword78 = "C	C" or "C|C" or "C	G" or "C|G"
keyword79 = "rs6603272"
keyword80 = "G	G" or "G|G" or "G	T" or "G|T"
keyword81 = "rs17883192"
keyword82 = "C	C" or "C|C" or "C	G" or "C|G"
keyword83 = "rs165599"
keyword84 = "G	G" or "G|G"
# Longevity
keyword85 = "rs3758391"
keyword86 = "C	T" or "C|T" or "T	T" or "T|T"
keyword87 = "rs5882"
keyword88 = "A	A" or "A|A" or "G	G" or "G|G"
keyword89 = "rs1042522"
keyword90 = "C	C" or "C|C" or "C	G" or "C|G"
keyword91 = "rs3803304"
keyword92 = "C	C" or "C|C" or "C	G" or "C|G" or "G	G" or "G|G"
keyword93 = "rs6873545"
keyword94 = "C	C" or "C|C"
keyword95 = "rs4590183"
keyword96 = "C	C" or "C|C"
keyword97 = "rs1556516"
keyword98 = "C	C" or "C|C" or "C	G" or "C|G" or "G	G" or "G|G"
keyword99 = "rs7137828"
keyword100 = "C	C" or "C|C" or "C	T" or "C|T" or "T	T" or "T|T"
keyword101 = "rs1627804"
keyword102 = "C	C" or "C|C" or "A	A" or "A|A" or "A	C" or "A|C"
keyword103 = "rs7844965"
keyword104 = "A	G" or "A|G" or "A	A" or "A|A" or "G	G" or "G|G"
keyword105 = "rs61978928"
keyword106 = "C	C" or "C|C" or "C	T" or "C|T" or "T	T" or "T|T"
keyword107 = "rs28926173"
keyword108 = "C	C" or "C|C" or "C	T" or "C|T" or "T	T" or "T|T"
keyword109 = "rs146254978"
keyword110 = "C	C" or "C|C" or "C	T" or "C|T" or "T	T" or "T|T"
keyword111 = "rs139137459"
keyword112 = "A	G" or "A|G" or "A	A" or "A|A" or "G	G" or "G|G"
# Immunity
keyword113 = "rs333"
keyword114 = "46373456"
# Intelligence
keyword115 = "rs28379706"
keyword116 = "T	T" or "T|T" or "C	T" or "C|T" or "C	C" or "C|C"
keyword117 = "rs363039"
keyword118 = "A	G" or "A|G" or "C	C" or "C|C"
keyword119 = "rs4680"
keyword120 = "A	A" or "A|A"
# Muscular Performance
keyword121 = "rs1815739"
keyword122 = "C	C" or "C|C" or "C	T" or "C|T"
keyword123 = "rs1805086"
keyword124 = "C	C" or "C|C" or "C	T" or "C|T"
# OCD
keyword125 = "rs4570625"
keyword126 = "G	G" or "G|G"
keyword127 = "rs4565946"
keyword128 = "C	C" or "C|C"
with open(filename, 'r') as file:
    lines = file.readlines()
# Bipolar Disorder Detect
Bipolar_Disorder1 = [i+1 for i, line in enumerate(lines) if keyword1 in line and keyword2 in line]
Bipolar_Disorder2 = [i+1 for i, line in enumerate(lines) if keyword3 in line and keyword4 in line]
Bipolar_Disorder3 = [i+1 for i, line in enumerate(lines) if keyword5 in line and keyword6 in line]
Bipolar_Disorder4 = [i+1 for i, line in enumerate(lines) if keyword7 in line and keyword8 in line]
Bipolar_Disorder5 = [i+1 for i, line in enumerate(lines) if keyword9 in line and keyword10 in line]
Bipolar_Disorder6 = [i+1 for i, line in enumerate(lines) if keyword11 in line and keyword12 in line]
Bipolar_Disorder7 = [i+1 for i, line in enumerate(lines) if keyword13 in line and keyword14 in line]
Bipolar_Disorder8 = [i+1 for i, line in enumerate(lines) if keyword15 in line and keyword16 in line]
Bipolar_Disorder9 = [i+1 for i, line in enumerate(lines) if keyword17 in line and keyword18 in line]
Bipolar_Disorder10 = [i+1 for i, line in enumerate(lines) if keyword19 in line and keyword20 in line]
Bipolar_Disorder11 = [i+1 for i, line in enumerate(lines) if keyword21 in line and keyword22 in line]
Bipolar_Disorder12 = [i+1 for i, line in enumerate(lines) if keyword23 in line and keyword24 in line]
# Alzheimer's Detect
Alzheimers1 = [i+1 for i, line in enumerate(lines) if keyword25 in line and keyword26 in line]
Alzheimers2 = [i+1 for i, line in enumerate(lines) if keyword27 in line and keyword28 in line]
Alzheimers3 = [i+1 for i, line in enumerate(lines) if keyword29 in line and keyword30 in line]
Alzheimers4 = [i+1 for i, line in enumerate(lines) if keyword31 in line and keyword32 in line]
# Autism Detect
Autism1 = [i+1 for i, line in enumerate(lines) if keyword33 in line and keyword34 in line]
Autism2 = [i+1 for i, line in enumerate(lines) if keyword35 in line and keyword36 in line]
Autism3 = [i+1 for i, line in enumerate(lines) if keyword37 in line and keyword38 in line]
Autism4 = [i+1 for i, line in enumerate(lines) if keyword39 in line and keyword40 in line]
Autism5 = [i+1 for i, line in enumerate(lines) if keyword41 in line and keyword42 in line]
Autism6 = [i+1 for i, line in enumerate(lines) if keyword43 in line and keyword44 in line]
Autism7 = [i+1 for i, line in enumerate(lines) if keyword45 in line and keyword46 in line]
Autism8 = [i+1 for i, line in enumerate(lines) if keyword47 in line and keyword48 in line]
Autism9 = [i+1 for i, line in enumerate(lines) if keyword49 in line and keyword50 in line]
Autism10 = [i+1 for i, line in enumerate(lines) if keyword51 in line and keyword52 in line]
Autism11 = [i+1 for i, line in enumerate(lines) if keyword53 in line and keyword54 in line]
Autism12 = [i+1 for i, line in enumerate(lines) if keyword55 in line and keyword56 in line]
Autism13 = [i+1 for i, line in enumerate(lines) if keyword57 in line and keyword58 in line]
Autism14 = [i+1 for i, line in enumerate(lines) if keyword59 in line and keyword60 in line]
Autism15 = [i+1 for i, line in enumerate(lines) if keyword61 in line and keyword62 in line]
Autism16 = [i+1 for i, line in enumerate(lines) if keyword63 in line and keyword64 in line]
Autism17 = [i+1 for i, line in enumerate(lines) if keyword65 in line and keyword66 in line]
# Schizophrenia Detect
Schizophrenia1 = [i+1 for i, line in enumerate(lines) if keyword67 in line and keyword68 in line]
Schizophrenia2 = [i+1 for i, line in enumerate(lines) if keyword69 in line and keyword70 in line]
Schizophrenia3 = [i+1 for i, line in enumerate(lines) if keyword71 in line and keyword72 in line]
Schizophrenia4 = [i+1 for i, line in enumerate(lines) if keyword73 in line and keyword74 in line]
Schizophrenia5 = [i+1 for i, line in enumerate(lines) if keyword75 in line and keyword76 in line]
Schizophrenia6 = [i+1 for i, line in enumerate(lines) if keyword77 in line and keyword78 in line]
Schizophrenia7 = [i+1 for i, line in enumerate(lines) if keyword79 in line and keyword80 in line]
Schizophrenia8 = [i+1 for i, line in enumerate(lines) if keyword81 in line and keyword82 in line]
Schizophrenia9 = [i+1 for i, line in enumerate(lines) if keyword83 in line and keyword84 in line]
# Longevity Detect
Longevity1 = [i+1 for i, line in enumerate(lines) if keyword85 in line and keyword86 in line]
Longevity2 = [i+1 for i, line in enumerate(lines) if keyword87 in line and keyword88 in line]
Longevity3 = [i+1 for i, line in enumerate(lines) if keyword89 in line and keyword90 in line]
Longevity4 = [i+1 for i, line in enumerate(lines) if keyword91 in line and keyword92 in line]
Longevity5 = [i+1 for i, line in enumerate(lines) if keyword93 in line and keyword94 in line]
Longevity6 = [i+1 for i, line in enumerate(lines) if keyword95 in line and keyword96 in line]
Longevity7 = [i+1 for i, line in enumerate(lines) if keyword97 in line and keyword98 in line]
Longevity8 = [i+1 for i, line in enumerate(lines) if keyword99 in line and keyword100 in line]
Longevity9 = [i+1 for i, line in enumerate(lines) if keyword101 in line and keyword102 in line]
Longevity10 = [i+1 for i, line in enumerate(lines) if keyword103 in line and keyword104 in line]
Longevity11 = [i+1 for i, line in enumerate(lines) if keyword105 in line and keyword106 in line]
Longevity12 = [i+1 for i, line in enumerate(lines) if keyword107 in line and keyword108 in line]
Longevity13 = [i+1 for i, line in enumerate(lines) if keyword109 in line and keyword112 in line]
# Immunity Detect
Immunity1 = [i+1 for i, line in enumerate(lines) if keyword113 in line and keyword114 in line]
# Intelligence Detect
Intelligence1 = [i+1 for i, line in enumerate(lines) if keyword115 in line and keyword116 in line]
Intelligence2 = [i+1 for i, line in enumerate(lines) if keyword117 in line and keyword118 in line]
Intelligence3 = [i+1 for i, line in enumerate(lines) if keyword119 in line and keyword120 in line]
# Muscular Performance Detect
Muscular_Performance1 = [i+1 for i, line in enumerate(lines) if keyword121 in line and keyword122 in line]
Muscular_Performance2 = [i+1 for i, line in enumerate(lines) if keyword123 in line and keyword124 in line]
# OCD Detect
OCD1 = [i+1 for i, line in enumerate(lines) if keyword123 in line and keyword124 in line]
OCD2 = [i+1 for i, line in enumerate(lines) if keyword125 in line and keyword126 in line]
# If Bipolar Disorder
if Bipolar_Disorder1:
    print(f"You have a trait which is associated with Bipolar Disorder | rs1006737 with the genotype of (A;A) https://www.snpedia.com/index.php/rs1006737")
if Bipolar_Disorder2:
    print(f"You have a trait which is associated with Bipolar Disorder | rs4027132 with the genotype of (A;A) or (A;G) https://www.snpedia.com/index.php/rs4027132")
if Bipolar_Disorder3:
    print(f"You have a trait which is associated with Bipolar Disorder | rs7570682 with the genotype of (A;A) or (A;G) https://www.snpedia.com/index.php/rs7570682")
if Bipolar_Disorder4:
    print(f"You have a trait which is associated with Bipolar Disorder | rs1375144 with the genotype of (C;C) https://www.snpedia.com/index.php/rs1375144")
if Bipolar_Disorder5:
    print(f"You have a trait which is associated with Bipolar Disorder | rs683395 with the genotype of (C;T) https://www.snpedia.com/index.php/rs683395")
if Bipolar_Disorder6:
    print(f"You have a trait which is associated with Bipolar Disorder | rs2609653 with the genotype of (C;T) or (C;C) https://www.snpedia.com/index.php/rs2609653")
if Bipolar_Disorder7:
    print(f"You have a trait which is associated with Bipolar Disorder | rs10982256 with the genotype of (C;C) https://www.snpedia.com/index.php/rs10982256")
if Bipolar_Disorder8:
    print(f"You have a trait which is associated with Bipolar Disorder | rs11622475 with the genotype of (C;C) https://www.snpedia.com/index.php/rs11622475")
if Bipolar_Disorder9:
    print(f"You have a trait which is associated with Bipolar Disorder | rs1344484 with the genotype of (T;T) https://www.snpedia.com/index.php/rs1344484")
if Bipolar_Disorder10:
    print(f"You have a trait which is associated with Bipolar Disorder | rs2953145 with the genotype of (C;G) or (G;G) https://www.snpedia.com/index.php/rs2953145")
if Bipolar_Disorder11:
    print(f"You have a trait which is associated with Bipolar Disorder | rs420259 with the genotype of (T;T) https://www.snpedia.com/index.php/rs420259")
if Bipolar_Disorder12:
    print(f"You have a trait which is associated with Bipolar Disorder | rs4276227 with the genotype of (C;C) https://www.snpedia.com/index.php/rs4276227")
# If Alzheimer's Disease
if Alzheimers1:
    print(f"You have a trait which is associated with Alzheimer's Disease | rs429358 with the genotype of (C;C) or (C;T) https://www.snpedia.com/index.php/rs429358")
if Alzheimers2:
    print(f"You have a trait which is associated with Alzheimer's Disease | rs145999145 with the genotype of (A;A) or (A;G) https://www.snpedia.com/index.php/rs145999145")
if Alzheimers3:
    print(f"You have a trait which is associated with Alzheimer's Disease | rs908832 with the genotype of (A;A) https://www.snpedia.com/index.php/rs908832")
if Alzheimers4:
    print(f"You have a trait which is associated with resistance to Alzheimer's Disease | rs63750847 with the genotype of (A;A) or (A;G) https://www.snpedia.com/index.php/rs63750847")
# If Autism
if Autism1:
    print(f"You have a trait which is associated with Autism | rs1858830 with the genotype of (C;C) or (C;G) https://www.snpedia.com/index.php/rs1858830")
if Autism2:
    print(f"You have a trait which is associated with Autism | rs2710102 with the genotype of (C;C) or (C;T) https://www.snpedia.com/index.php/rs2710102")
if Autism3:
    print(f"You have a trait which is associated with Autism | rs7794745 with the genotype of (A;T) or (T;T) https://www.snpedia.com/index.php/rs7794745")
if Autism4:
    print(f"You have a trait which is associated with Autism | rs1322784 https://www.snpedia.com/index.php/rs1322784")
if Autism5:
    print(f"You have a trait which is associated with Autism | rs265981 with the genotype of (A;G) or (G;G) https://www.snpedia.com/index.php/rs265981")
if Autism6:
    print(f"You have a trait which is associated with Autism | rs4532 with the genotype of (C;T) or (T;T) https://www.snpedia.com/index.php/rs4532")
if Autism7:
    print(f"You have a trait which is associated with Autism | rs686 with the genotype of (A;G) or (A;A) https://www.snpedia.com/index.php/rs686")
if Autism8:
    print(f"You have a trait which is associated with Autism | rs1143674 with the genotype of (A;G) or (A;A) https://www.snpedia.com/index.php/rs1143674")
if Autism9:
    print(f"You have a trait which is associated with Autism | rs6807362 with the genotype of (C;C) https://www.snpedia.com/index.php/rs6807362")
if Autism10:
    print(f"You have a trait which is associated with Autism | rs757972971 with the genotype of (A;G) or (A;A) https://www.snpedia.com/index.php/rs757972971")
if Autism11:
    print(f"You have a trait which is associated with Autism | rs2217262 with the genotype of (A;A) https://www.snpedia.com/index.php/rs2217262")
if Autism12:
    print(f"You have a trait which is associated with Autism | rs6766410 https://www.snpedia.com/index.php/rs6766410")
if Autism13:
    print(f"You have a trait which is associated with Autism | rs1445442 https://www.snpedia.com/index.php/rs1445442")
if Autism14:
    print(f"You have a trait which is associated with Autism | rs2421826 https://www.snpedia.com/index.php/rs2421826")
if Autism15:
    print(f"You have a trait which is associated with Autism | rs1358054 https://www.snpedia.com/index.php/rs1358054")
if Autism16:
    print(f"You have a trait which is associated with Autism | rs536861 https://www.snpedia.com/index.php/rs536861")
if Autism17:
    print(f"You have a trait which is associated with Autism | rs722628 https://www.snpedia.com/index.php/rs722628")
# If Schizophrenia
if Schizophrenia1:
    print(f"You have a trait which is associated with Schizophrenia | rs27388 with the genotype of (A;A) or (A;G) https://www.snpedia.com/index.php/rs27388")
if Schizophrenia2:
    print(f"You have a trait which is associated with Schizophrenia | rs2270641 with the genotype of (G;G) https://www.snpedia.com/index.php/rs2270641")
if Schizophrenia3:
    print(f"You have a trait which is associated with Schizophrenia | rs4129148 with the genotype of (C;C) or (C;G) https://www.snpedia.com/index.php/rs4129148")
if Schizophrenia4:
    print(f"You have a trait which is associated with Schizophrenia | rs28694718 with the genotype of (A;A) or (A;G) https://www.snpedia.com/index.php/rs28694718")
if Schizophrenia5:
    print(f"You have a trait which is associated with Schizophrenia | rs6422441 with the genotype of (C;C) or (C;T) https://www.snpedia.com/index.php/rs6422441")
if Schizophrenia6:
    print(f"You have a trait which is associated with Schizophrenia | rs28414810 with the genotype of (C;C) or (C;G) https://www.snpedia.com/index.php/rs28414810")
if Schizophrenia7:
    print(f"You have a trait which is associated with Schizophrenia | rs6603272 with the genotype of (G;G) or (G;T) https://www.snpedia.com/index.php/rs6603272")
if Schizophrenia8:
    print(f"You have a trait which is associated with Schizophrenia | rs17883192 with the genotype of (C;C) or (C;G) https://www.snpedia.com/index.php/rs17883192")
if Schizophrenia9:
    print(f"You have a trait which is associated with Schizophrenia | rs165599 with the genotype of (G;G) https://www.snpedia.com/index.php/rs165599")
# If Longevity
if Longevity1:
    print(f"You have a trait which is associated with Longevity | rs3758391 with the genotype of (C;T) or (T;T) https://www.snpedia.com/index.php/rs3758391")
if Longevity2:
    print(f"You have a trait which is associated with Longevity | rs5882 with the genotype of (A;A) or (G;G) https://www.snpedia.com/index.php/rs5882")
if Longevity3:
    print(f"You have a trait which is associated with Longevity | rs1042522 with the genotype of (C;C) or (C;G) https://www.snpedia.com/index.php/rs1042522")
if Longevity4:
    print(f"You have a trait which is associated with Longevity | rs3803304 https://www.snpedia.com/index.php/rs27388")
if Longevity5:
    print(f"You have a trait which is associated with Longevity | rs6873545 with the genotype of (C;C) https://www.snpedia.com/index.php/rs6873545")
if Longevity6:
    print(f"You have a trait which is associated with Longevity | rs4590183 with the genotype of (C;C) https://www.snpedia.com/index.php/rs4590183")
if Longevity7:
    print(f"You have a trait which is associated with Longevity | rs1556516 https://www.snpedia.com/index.php/rs1556516")
if Longevity8:
    print(f"You have a trait which is associated with Longevity | rs7137828 https://www.snpedia.com/index.php/rs7137828")
if Longevity9:
    print(f"You have a trait which is associated with Longevity | rs1627804 https://www.snpedia.com/index.php/rs1627804")
if Longevity10:
    print(f"You have a trait which is associated with Longevity | rs7844965 https://www.snpedia.com/index.php/rs7844965")
if Longevity11:
    print(f"You have a trait which is associated with Longevity | rs61978928 https://www.snpedia.com/index.php/rs61978928")
if Longevity12:
    print(f"You have a trait which is associated with Longevity | rs28926173 https://www.snpedia.com/index.php/rs28926173")
if Longevity13:
    print(f"You have a trait which is associated with Longevity | rs146254978 https://www.snpedia.com/index.php/rs146254978")
if Longevity13:
    print(f"You have a trait which is associated with Longevity | rs139137459 https://www.snpedia.com/index.php/rs139137459")
# If Immunity
if Immunity1:
    print(f"You have a trait which is associated with HIV Immunity | rs333 https://www.snpedia.com/index.php/rs333")
# If Intelligence
if Intelligence1:
    print(f"You have a trait which is associated with Intelligence | rs28379706 https://www.snpedia.com/index.php/rs28379706")
if Intelligence2:
    print(f"You have a trait which is associated with Intelligence | rs363039 with the genotype of (A;G) or (C;C) https://www.snpedia.com/index.php/rs363039")
if Intelligence3:
    print(f"You have a trait which is associated with Intelligence | rs4680 with the genotype of (A;A) https://www.snpedia.com/index.php/rs4680")
# If Muscular Performance
if Muscular_Performance1:
    print(f"You have a trait which is associated with Muscular Performance | rs1815739 with the genotype of (C;C) or (C;T) https://www.snpedia.com/index.php/rs1815739")
if Muscular_Performance2:
    print(f"You have a trait which is associated with Muscular Performance | rs1805086 with the genotype of (C;C) or (C;T) https://www.snpedia.com/index.php/rs1805086")
# If OCD
if OCD1:
    print(f"You have a trait which is associated with OCD | rs4570625 with the genotype of (G;G) https://www.snpedia.com/index.php/rs4570625")
if OCD2:
    print(f"You have a trait which is associated with OCD | rs4565946 with the genotype of (C;C) https://www.snpedia.com/index.php/rs4565946")
