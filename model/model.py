from database.DAO import DAO
import networkx as nx

from model import rotta
from model.rotta import Rotta


class Model:
    def __init__(self):
        self.aeroporti = DAO.getAllAeroporti()
        self._grafo = nx.DiGraph()
        self._idMapAeroporti = {}
        self._rotte=set()
        for a in self.aeroporti:
            self._idMapAeroporti[a.ID] = a

    def buildGraph(self, dist_min):
        self._grafo.clear()
        self._grafo.add_nodes_from(self.aeroporti)
        self.addEdges(dist_min)


    def addEdges(self, dist_min):
        self._rotte = DAO.getAllRotte()
        for r in self._rotte:
            if r.media > dist_min:
                p = self._idMapAeroporti[r.ORIGIN_AIRPORT_ID]
                a = self._idMapAeroporti[r.DESTINATION_AIRPORT_ID]
                self._grafo.add_edge(p, a, weight = r.media)

    def getNumEdges(self):
        return self._grafo.number_of_edges()

    def getNumNodes(self):
        return self._grafo.number_of_nodes()

    def getAllEdges(self):
        return self._grafo.edges()