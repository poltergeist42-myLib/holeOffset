#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Infos
=====

   :Projet:             
   :Nom du fichier:     holeOffset.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20170811

####

   :Licence:            CC-BY-NC-SA
   :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

####

    :dev language:      Python 3.6
    :framework:         
    
####

Descriptif
==========

    :Projet:            
                        
    :Fichiers:          holeOffset.py permet de parcourrir un fichier de perçage généré
                        par les logiciel de CIAO et de corriger les coordonées de chacun
                        des trous en fonction des repères identifiés sur le PCB.
    

####

lexique
=======

   :**v_**:                 variable
   :**l_**:                 list
   :**t_**:                 tuple
   :**d_**:                 dictionnaire
   :**f_**:                 fonction
   :**C_**:                 Class
   :**i_**:                 Instance
   :**m_**:                 Matrice
   
####

"""
from __future__ import absolute_import
import os, sys
sys.path.insert(0,'..')         # ajouter le repertoire precedent au path (non définitif)
                                # pour pouvoir importer les modules et paquets parent
try :
    from devChk.devChk import C_DebugMsg
    v_dbgChk = True
    i_dbg = C_DebugMsg()
   
except ImportError :
    print( "module devChk non present" )
    v_dbgChk = False

import argparse

class C_HoleOffset( object ) :
    """ permet de parcourrir un fichier perçage de logiciel de CIAO et de corriger les
        coordonées de chacun des trous en fonction des repères identifiés sur le PCB.
    """
    def __init__( self ) :
        """ **__init__()**
        
            Creation et initialisation des variables globales de cette Class
        """
        self.v_dir              = os.getcwd()
                                # os.getcwd() : permet de recuperer le chemin
                                # du repertoire local
        self.v_fileFormat       = ".drl"
        self.v_file             = ''
        self.v_fileName         = ''
        self.v_offsetFile       = ''
        self.v_offsetFileName   = ''
        self.v_xOffset          = 0.0
        self.v_yOffset          = 0.0
        self.v_segmentOA        = 0.0
        self.v_segmentAB        = 0.0
        
####
        
    def __del__( self ) :
        """ **__del__()**
        
            Permet de terminer proprement l'instance de la Class courante
        
            il faut utilise : ::
            
                del [nom_de_l'_instance]
                
            *N.B :* Si l'instance n'est plus utilisee, cette methode est appellee 
            automatiquement.
        """
        ## dbg
        v_dbg = 1
        v_dbg2 = 1
        f_dbg(v_dbg2, "__del__", self.__del__)
        
        ## Action
        v_className = self.__class__.__name__

        ## dbg
        f_dbg( v_dbg, v_className, v_tittle = False  )
              
####

    def f_setOffsetFileName(self, v_fileName) :
        """ Permet de créer le nom du nouveau fichier de perçage """
        self.v_offsetFileName = "offset_{}".format( v_fileName )
        self.v_offsetFile = os.path.join(self.v_dir, self.v_offsetFileName)
        return self.v_offsetFile
        
####

    def f_setOffset(self, v_xOffset=0, v_yOffset=0) :
        """ renseigne les varriables de class : v_xOffset et v_yOffset """
        if (not self.v_xOffset) and (not self.v_yOffset) :
            if v_xOffset :
                self.v_xOffset = v_xOffset
            
            if v_yOffset :
                self.v_yOffset = v_yOffset

####

    def f_setOffsetToHole(self, v_xValue, v_yValue) :
        """ Applique l'offset sur le coordonées X et Y de chacun des troues """
        return "X{}Y{}\n".format(v_xValue + self.v_xOffset, v_yValue + self.v_yOffset)

####

    def f_setMireDimension(self, v_segmentOA, v_segmentAB) :
        """ Permet de fixer la distance entre l'origine et la mire A (segmentOA) et la
            distance entre la mire A et la mire B (segmentAB)
        """
        self.v_segmentOA = v_segmentOA
        self.v_segmentAB = v_segmentAB
        
    def f_getMireDimension(self) :
        """ retourne la distance entre l'origine et la mire A (segmentOA) et la
            distance entre la mire A et la mire B (segmentAB)
        """
        return self.v_segmentOA, self.v_segmentAB
    
    def f_setNewDrlFile(self, v_file) :
        """ Parcour le fichier de perçage en créant un second fichier contenant les
            nouvelles coordonées des troues
        """
        ## dbg
        v_dbg = 1
        v_dbg2 = 1
        f_dbg(v_dbg2, "f_setNewDrlFile", self.f_setNewDrlFile)

        ## Action
        v_xIndex = 0
        v_yIndex = 0
        v_xChaine = 'X'
        v_yChaine = 'Y'
        v_newDrlFileName = self.f_setOffsetFileName(self.v_fileName)

        # v_showVal = ''
        # v_count = 1
        v_chk = True      
        try :
            v_drlParse = open(v_file, 'r')
            v_chkWr = True
            try :
                os.remove( v_newDrlFileName )               
                v_wrDrl = open(v_newDrlFileName, 'a')
            
                for v_line in v_drlParse : 
                    v_xValue = 0.0
                    v_yValue = 0.0
                    if (not v_xChaine in v_line) or (not v_yChaine in v_line) :
                        v_wrDrl.write( v_line )
                        # v_showVal = v_line
                    else :
                        if (v_xChaine in v_line) and (v_yChaine in v_line) :
                            for i in range( len(v_line) ) :
                                if v_line[i] == v_xChaine :
                                    v_xIndex = i              
                                if v_line[i] == v_yChaine :
                                    v_yIndex = i
                                    v_xValue = eval(v_line[v_xIndex+1:v_yIndex])
                                    v_yValue = eval(v_line[v_yIndex+1:])
                                        
                    if v_xValue or v_yValue :
                        v_wrDrl.write(self.f_setOffsetToHole(v_xValue, v_yValue))
                        # v_showVal = self.f_setOffsetToHole(v_xValue, v_yValue)
                        
                    # print("{} - {} --> {}".format(v_count, v_line, v_showVal))
                    # v_count += 1
                    
        
            except FileNotFoundError :
                print("fichier : {} --> non trouve".format(v_wrDrl))
                v_chkWr = False               

            finally :
                if v_chkWr : v_wrDrl.close()
         
        except FileNotFoundError :
            print("fichier : {} --> non trouve".format(v_drlParse))
            v_chk = False           

        finally :
            if v_chk : v_drlParse.close()
    
####

## Accessoires
def f_dbg( v_bool, v_data, v_tittle = False  ) :
    """ Fonction de traitemant du debug """
    if v_dbgChk and v_tittle :
        i_dbg.dbgPrint( v_bool, v_tittle, v_data )
        
    elif v_dbgChk and not v_tittle :
        i_dbg.dbgDel( v_bool, v_data)
        

## Main                       
def main() :
    """ Fonction principale """
    parser = argparse.ArgumentParser()
    parser.add_argument( "-d", "--debug", action='store_true', help="activation du mode debug")
    # parser.add_argument( "-t", "--test", action='store_true', help="activation du mode Test")
                        
    args = parser.parse_args()
    
    if args.debug :
        print( "Mode Debug active" )
        i_dbg.f_setAffichage( True )
    
    v_localWorkDir = input("Entrez le chemin absolu du dossier ou se trouve le fichier de perçage : ")
    # i_ist = C_HoleOffset()
    
    # i_ist.f_getDrlPath(v_localWorkDir)
    # i_ist.f_setOffset(1, 1)
    # i_ist.f_setNewDrlFile(i_ist.v_file)
    
    print("\n\n\t\t fin de la sequence ")
    

if __name__ == '__main__':
    main()
