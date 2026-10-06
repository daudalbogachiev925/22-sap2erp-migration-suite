import pandas as pd
from transform.transform import rename_fields, clean

def test_rename():
    df = pd.DataFrame({'KUNNR':['1'], 'NAME1':['A']})
    mapping = {'fields': {'KUNNR':'code','NAME1':'full_name'}}
    r = rename_fields(df, mapping)
    assert 'code' in r.columns
    assert 'full_name' in r.columns

def test_clean_dedup():
    df = pd.DataFrame({'code':['1','1','2'], 'full_name':['A','A','B']})
    r = clean(df)
    assert len(r) == 2
