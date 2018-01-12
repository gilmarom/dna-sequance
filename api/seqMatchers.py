

class matchers:

    @staticmethod
    def dnaMatch(argument = str):
        switcher = {
                    'a': 't',
                    
                    't': 'a', 
                
                    "c": 'g',
                
                    'g': 'c'           
                    }
            
        return switcher.get(argument)

    @staticmethod 
    def rnaMatch(argument = str):
        
        switcher = {
                    "t" : "a",
                    "a" : "u",
                    "c" : "g",
                    "g" : "c",
                    }  
        return switcher.get(argument)

    @staticmethod
    def aminoMatch(argument = str):

        switcher = {
                "uuu":"phenylalanine", "uuc":"phenylalanine","uua":"leucine","uug":"leucine",
                "ucu":"serine","ucc":"serine","uca":"serine","ucg":"serine",
                "uau":"tyrosine","uac":"tyrosine","uaa":"stop","uag":"stop",
                "ugu":"cysteine", "ugc":"cysteine", "uga":"stop","ugg":"tryptophan",
                "cuu":"leucine","cuc":"leucine","cua":"leucine","cug":"leucine",
                "ccu":"proline","ccc":"proline","cca":"proline","ccg":"proline",
                "cau":"histidine","cac":"histidine","caa":"glutamine","cag":"glutamine",
                "cgu":"arginine","cgc":"arginine","cga":"arginine","cgg":"arginine",
                "auu":"isoleucine","auc":"isoleucine","aua":"isoleucine","aug":"methionine", 
                "acu":"threonine","acc":"threonine","aca":"threonine","acg":"threonine", 
                "aau":"asparagine","aac":"asparagine","aaa":"lysine","aag":"lysine", 
                "agu":"serine","agc":"serine","aga":"arginine","agg":"arginine", 
                "guu":"valine","guc":"valine","gua":"valine","gug":"valine",  
                "gcu":"alanine","gcc":"alanine","gca":"alanine","gcg":"alanine",  
                "gau":"aspartate","gac":"aspartate","gaa":"glutamate","gag":"glutamate",  
                "ggu":"glycine","ggc":"glycine","gga":"glycine","ggg":"glycine",              
                }      
        
       
        return switcher.get(argument)    
