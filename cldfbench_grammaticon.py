import pathlib

from cldfbench import Dataset as BaseDataset


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "grammaticon"

    def cldf_specs(self):  # A dataset must declare all CLDF sets it creates.
        return super().cldf_specs()

    def cmd_download(self, args):
        """
        Download files to the raw/ directory. You can use helpers methods of `self.raw_dir`, e.g.

        >>> self.raw_dir.download(url, fname)
        """
        excel_sheets = [
            'Concepthierarchy.xlsx',
            'Concepts.xlsx',
            'Concepts_metafeatures.xlsx',
            'Feature_lists.xlsx',
            'Features.xlsx',
            'Metafeatures.xlsx',
            'x_Concepthierarchy.xlsx',
            'x_Concepts_Metafeatures.xlsx',
        ]
        for sheet in excel_sheets:
            self.raw_dir.xlsx2csv(sheet)

    def cmd_makecldf(self, args):
        """
        Convert the raw data to a CLDF dataset.

        >>> args.writer.objects['LanguageTable'].append(...)
        """
