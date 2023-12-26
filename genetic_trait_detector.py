"""
genetic trait detection library
"""
import sys


class Rsid:
    """genetic rsid detector class"""

    def __init__(
        self,
        rsid: str,
        alleles: tuple | str,
        association: str,
    ) -> None:
        """constructor"""
        self.rsid = rsid
        self.alleles = alleles if isinstance(alleles, tuple) else (alleles,)
        self.association = association

    def detect(self, line: str) -> bool:
        """detect this rsid in the given line of dna data"""
        return self.rsid in line and any(y in line for y in self.allele_match_set)

    def __str__(self) -> str:
        """string representation"""
        return f"<Rsid[{self.rsid}]({self.association})>"

    def __repr__(self) -> str:
        """repl representation"""
        return self.__str__()

    @property
    def single_allele(self) -> bool:
        """if this is a single allele match"""
        return len(self.alleles) == 1

    @property
    def allele_match_set(self) -> tuple:
        """form a set of different formats of alleles"""

        def _set(allele: str) -> tuple:
            """form a set of allele formats"""
            if ";" in allele:
                a0, a1 = allele.upper().split(";")
                return (f"{a0}	{a1}", f"{a0}|{a1}", f"{a0}{a1}")
            return (allele,)

        tuples = ()
        for allele in self.alleles:
            tuples += _set(allele)
        return tuples

    @property
    def url(self) -> str:
        """return the url to snpedia"""
        return f"https://www.snpedia.com/index.php/{self.rsid}"

    @property
    def info(self) -> str:
        """return an informational string about this rsid when detected"""
        allele = (
            f"with the genotype of ({self.alleles[0]}) " if self.single_allele else ""
        )
        return (
            f"You have a trait which is associated with {self.association} | "
            f"{self.rsid} {allele}{self.url}"
        )


class Trait:
    """traits enum class"""

    alzheimer = "Alzheimer's Disease"
    autism = "Autism"
    bpd = "Bipolar Disorder"
    hiv_immunity = "HIV Immunity"
    intelligence = "Intelligence"
    longevity = "Longevity"
    metabolism = "Metabolism"
    muscular_performance = "Muscular Performance"
    ocd = "OCD"
    schizo = "Schizophrenia"


_RSIDS = [
    ("rs1006737", "A;A", Trait.bpd),
    ("rs4027132", "A;A", Trait.bpd),
    ("rs7570682", "A;A", Trait.bpd),
    ("rs1375144", "C;C", Trait.bpd),
    ("rs683395", "C;T", Trait.bpd),
    ("rs2609653", "C;T", Trait.bpd),
    ("rs10982256", "C;C", Trait.bpd),
    ("rs11622475", "C;C", Trait.bpd),
    ("rs1344484", "T;T", Trait.bpd),
    ("rs2953145", "C;G", Trait.bpd),
    ("rs420259", "T;T", Trait.bpd),
    ("rs4276227", "C;C", Trait.bpd),
    ("rs4027132", "A;G", Trait.bpd),
    ("rs2609653", "C;C", Trait.bpd),
    ("rs2953145", "G;G", Trait.bpd),
    ("rs429358", "C;C", Trait.alzheimer),
    ("rs145999145", "A;A", Trait.alzheimer),
    ("rs908832", "A;A", Trait.alzheimer),
    ("rs63750847", "A;A", f"resistance to {Trait.alzheimer}"),
    ("rs429358", "C;T", f"resistance to {Trait.alzheimer}"),
    ("rs145999145", "A;G", f"resistance to {Trait.alzheimer}"),
    ("rs63750847", "A;G", f"resistance to {Trait.alzheimer}"),
    ("rs1858830", "C;C", Trait.autism),
    ("rs2710102", "C;C", Trait.autism),
    ("rs7794745", "A;T", Trait.autism),
    ("rs1322784", ("C;C", "C;T", "T;T"), Trait.autism),
    ("rs265981", "A;G", Trait.autism),
    ("rs4532", "C;T", Trait.autism),
    ("rs686", "A;G", Trait.autism),
    ("rs1143674", "A;A", Trait.autism),
    ("rs6807362", "C;C", Trait.autism),
    ("rs757972971", "A;A", Trait.autism),
    ("rs2217262", "A;A", Trait.autism),
    ("rs6766410", ("A;A", "A;C", "C;C"), Trait.autism),
    ("rs1445442", ("A;A", "A;G", "G;G"), Trait.autism),
    ("rs2421826", ("C;T", "T;T", "C;C"), Trait.autism),
    ("rs1358054", ("G;G", "G;T", "T;T"), Trait.autism),
    ("rs536861", ("A;A", "A;C", "C;C"), Trait.autism),
    ("rs722628", ("A;A", "A;G", "G;G"), Trait.autism),
    ("rs1858830", "C;G", Trait.autism),
    ("rs2710102", "G;G", Trait.autism),
    ("rs7794745", "T;T", Trait.autism),
    ("rs265981", "G;G", Trait.autism),
    ("rs4532", "T;T", Trait.autism),
    ("rs686", "A;A", Trait.autism),
    ("rs1143674", "A;A", Trait.autism),
    ("rs757972971", "A;A", Trait.autism),
    ("rs27388", "A;A", Trait.schizo),
    ("rs2270641", "G;G", Trait.schizo),
    ("rs4129148", "C;C", Trait.schizo),
    ("rs28694718", "A;A", Trait.schizo),
    ("rs6422441", "C;C", Trait.schizo),
    ("rs28414810", "C;C", Trait.schizo),
    ("rs6603272", "G;G", Trait.schizo),
    ("rs17883192", "C;C", Trait.schizo),
    ("rs165599", "G;G", Trait.schizo),
    ("rs27388", "A;G", Trait.schizo),
    ("rs4129148", "C;G", Trait.schizo),
    ("rs28694718", "A;G", Trait.schizo),
    ("rs6422441", "C;T", Trait.schizo),
    ("rs28414810", "C;G", Trait.schizo),
    ("rs6603272", "G;T", Trait.schizo),
    ("rs17883192", "C;G", Trait.schizo),
    ("rs3758391", "C;T", Trait.longevity),
    ("rs5882", "A;A", Trait.longevity),
    ("rs1042522", "C;C", Trait.longevity),
    ("rs3803304", ("C;C", "C;G", "G;G"), Trait.longevity),
    ("rs6873545", "C;C", Trait.longevity),
    ("rs4590183", "C;C", Trait.longevity),
    ("rs1556516", ("C;C", "C;G", "G;G"), Trait.longevity),
    ("rs7137828", ("C;C", "C;T", "T;T"), Trait.longevity),
    ("rs1627804", ("C;C", "A;A", "A;C"), Trait.longevity),
    ("rs7844965", ("A;G", "A;A", "G;G"), Trait.longevity),
    ("rs61978928", ("C;C", "C;T", "T;T"), Trait.longevity),
    ("rs28926173", ("C;C", "C;T", "T;T"), Trait.longevity),
    ("rs146254978", ("C;C", "C;T", "T;T"), Trait.longevity),
    ("rs139137459", ("A;G", "A;A", "G;G"), Trait.longevity),
    ("rs3758391", "T;T", Trait.longevity),
    ("rs5882", "A;G", Trait.longevity),
    ("rs1042522", "C;G", Trait.longevity),
    ("rs333", ("46373456",), Trait.hiv_immunity),
    ("rs28379706", ("T;T", "C;T", "C;C"), Trait.intelligence),
    ("rs363039", "A;G", Trait.intelligence),
    ("rs4680", "A;A", Trait.intelligence),
    ("rs363039", "C;C", Trait.intelligence),
    ("rs1815739", "C;C", Trait.muscular_performance),
    ("rs1805086", "C;C", Trait.muscular_performance),
    ("rs1815739", "C;T", Trait.muscular_performance),
    ("rs1805086", "C;T", Trait.muscular_performance),
    ("rs4570625", "G;G", Trait.ocd),
    ("rs4565946", "C;C", Trait.ocd),
    ("rs1801131", ("A;C", "C;C"), Trait.metabolism),
    ("rs1801133", ("C;T", "T;T"), Trait.metabolism),
    ("rs2282679", ("A;C", "C;C"), Trait.metabolism),
    ("rs12785878", ("G;T", "T;T"), Trait.metabolism),
    ("rs1799945", "F;G", Trait.metabolism),
    ("rs4988235", "C;C", Trait.metabolism),
    ("rs182549", "C;C", Trait.metabolism),
    ("rs2187668", "A;A", Trait.metabolism),
    ("rs5030858", "T;T", Trait.metabolism),
    ("rs12913832", "G;G", "Blue Eyes"),
    ("rs4988235", "C;C", "Lactose Intolerance"),
]
RSIDS = [Rsid(x[0], x[1], x[2]) for x in _RSIDS]


def parse_file(path: str) -> dict[str, str]:
    """parse a file into a dict that we can perform lookups with"""
    with open(path) as genes:
        return {x.split("\t")[0]: x for x in genes.readlines() if x.startswith("rs")}


def scan_genes(rsid_dict: dict[str, str]) -> list[Rsid]:
    """scan the given gene dictionary, returning a list of RSIDS that were detected"""
    return [x for x in RSIDS if x.rsid in rsid_dict and x.detect(rsid_dict[x.rsid])]


if __name__ == "__main__":
    filename = (
        sys.argv[1]
        if len(sys.argv) > 1
        else input("Enter the location of the DNA data file: ")
    )
    rsid_dict = parse_file(filename)
    rsids = scan_genes(rsid_dict)
    for rsid in rsids:
        print(rsid.info)
