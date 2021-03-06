# vim: fdm=indent
'''
author:     Fabio Zanini
date:       06/11/14
content:    Models for the hivwholeweb site.

            We are in a particular position, because we do not collect data
            from the users and store in a database, but we need to stream data.

            This makes our 'models' a bit odd.
'''
from flask_restful import Resource, abort



class Tree(Resource):
    def get(self, pname, region):
        from ....models import TreeModel
        try:
            return TreeModel(pname, region).get_json()
        except IOError:
            msg = "No tree for patient {} and region {} found".format(pname, region)
            abort(404, message=msg)


class Physiological(Resource):
    def get(self, pname):
        from ....models import PhysioModel
        try:
            return PhysioModel(pname).get_data(zipped=True)
        except IOError:
            msg = "No physiological data for patient {} found".format(pname)
            abort(404, message=msg)


class ViralLoad(Resource):
    def get(self, pname):
        from ....models import PhysioModel
        try:
            return PhysioModel(pname).get_data(zipped=True, obs=['viral load'])
        except IOError:
            msg = "No viral load data for patient {} found".format(pname)
            abort(404, message=msg)


class CellCount(Resource):
    def get(self, pname):
        from ....models import PhysioModel
        try:
            return PhysioModel(pname).get_data(zipped=True, obs=['CD4+ cell count'])
        except IOError:
            msg = "No CD4+ cell count data for patient {} found".format(pname)
            abort(404, message=msg)


class NTemplates(Resource):
    def get(self, pname):
        from ....models import NTemplatesModel
        try:
            return NTemplatesModel(pname).get_data()
        except IOError:
            msg = "No template numbers data for patient {} found".format(pname)
            abort(404, message=msg)


class ReferenceSequence(Resource):
    def get(self, pname, region='genomewide'):
        from ....models import GenomeModel
        try:
            return GenomeModel(pname, region).get_data()
        except IOError:
            msg = "No reference sequence for patient {} and region {} found".format(pname, region)
            abort(404, message=msg)


class Coverage(Resource):
    '''Coverage resource, both trajectories and single samples'''
    def get(self, psname, region='genomewide'):
        try:
            if '_' in psname:
                from ....models import CoverageModel
                return CoverageModel(psname, region).get_data()
            else:
                from ....models import CoverageTrajectoryModel
                return CoverageTrajectoryModel(psname, region).get_data()
        except IOError:
            msg = "No coverage data for {} and region {} found".format(psname, region)
            abort(404, message=msg)


class DivDiv(Resource):
    '''Divergence and diversity'''
    def get(self, pname, region):
        try:
            from ....models import DivdivModel
            return DivdivModel(pname, region).get_data()
        except IOError:
            msg = "No divergence/diversity data for {} and region {} found".format(pname, region)
            abort(404, message=msg)


class DivDivSliding(Resource):
    '''Divergence and diversity'''
    def get(self, pname):
        try:
            from ....models import DivdivLocalModel
            return DivdivLocalModel(pname).get_data()
        except IOError:
            msg = "No divergence/diversity data for {} found".format(pname)
            abort(404, message=msg)


class AlleleFrequencies(Resource):
    '''SNP resource, both trajectories and single samples'''
    def get(self, psname, region='genomewide', fmt='full'):
        try:
            if '_' in psname:
                from ....models import AlleleFrequencyModel
                return AlleleFrequencyModel(psname, region).get_data(fmt=fmt)
            else:
                from ....models import AlleleFrequencyTrajectoryModel
                return AlleleFrequencyTrajectoryModel(psname, region).get_data(fmt=fmt)
        except IOError:
            msg = "No SNP data for {} and region {} found".format(psname, region)
            abort(404, message=msg)


class Haplotypes(Resource):
    '''SNP resource, both trajectories and single samples'''
    def get(self, psname, region):
        try:
            if '_' in psname:
                from ....models import HaplotypePrecompiledModel
                return HaplotypePrecompiledModel(psname, region).get_data(format='json')
            else:
                from ....models import HaplotypePrecompiledTrajectoryModel
                return HaplotypePrecompiledTrajectoryModel(psname, region).get_data(format='json')
        except IOError:
            msg = "No haplotype data for {} and region {} found".format(psname, region)
            abort(404, message=msg)



