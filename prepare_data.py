import nltk
from data.utils import load_doc_karpathy,prepare_ref_caps_for_evaluate
from pathlib import Path
import json
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = list(set(stopwords.words('english')))
# MASKED_WORDS=[w for w in stop_words if w not in {'a','in','on','an','the'}]
MASKED_WORDS=[w for w in stop_words if w not in {'both','below','in','over','above','same','before','up','down','on','under','into',"haven't","weren't","hadn't","didn't","mustn't","she's","shan't","aren't","doesn't","at'll","it's","wasn't","won't","isn't","don't","hasn't","you'd","should've","shouldn't","couldn't","you've","you'll","you're","needn't","mightn't","wouldn't","hat'll","that'll"}]

pattern=r'\b('+'|'.join(MASKED_WORDS)+r')\b'

def prepare_training_data(karpathy_json,annot_path):
    if karpathy_json.split('/')[-1]=='dataset_coco.json':
        IS_COCO=True
    else:
        IS_COCO=False
    KARPATHY_DATA=load_doc_karpathy(json_file_path=karpathy_json,pattern=pattern,lower=True,is_coco=IS_COCO)   
    Path(annot_path).mkdir(parents=True, exist_ok=True)
    # KARPATHY_DATA['train']=KARPATHY_DATA['train'][:100]
    # KARPATHY_DATA['val']=KARPATHY_DATA['val'][:100]
    # KARPATHY_DATA['test']=KARPATHY_DATA['test'][:100]
    prepare_ref_caps_for_evaluate(KARPATHY_DATA['val'],annot_path+'/coco_karpathy_val_gt.json')
    prepare_ref_caps_for_evaluate(KARPATHY_DATA['test'],annot_path+'/coco_karpathy_test_gt.json')

    json.dump(KARPATHY_DATA['val'],open(annot_path+'/coco_karpathy_val.json','w'))
    json.dump(KARPATHY_DATA['train'],open(annot_path+'/coco_karpathy_train.json','w'))
    json.dump(KARPATHY_DATA['test'],open(annot_path+'/coco_karpathy_test.json','w'))
