from dotenv import load_dotenv
from googleapiclient.discovery import build
import csv, os, time, re

START_TIME = time.time()

load_dotenv()
YOUTUBE = build('youtube', 'v3', developerKey=os.getenv('API_KEY'))
comments = []

def process_replies(response_items):
    for response in response_items:
        comment = {}
        comment['comment'] = response['snippet']['textOriginal']
        comments.append(comment)

def process_comments(response_items):
    global comments

    for response in response_items:
        # top level comment
        comment = {}
        comment['comment'] = response['snippet']['topLevelComment']['snippet']['textOriginal']
        comments.append(comment)
        # check for replies
        if 'replies' in response.keys():
            parent_id = response['snippet']['topLevelComment']['id']
            request = YOUTUBE.comments().list(
                part='snippet',
                parentId=parent_id,
                maxResults=100
            )
            response = request.execute()
            process_replies(response['items'])

            # get the rest of the replies (for >100 replies)
            while response.get('nextPageToken', None):
                request = YOUTUBE.comments().list(
                    part='snippet',
                    parentId=parent_id,
                    maxResults=100,
                    pageToken=response['nextPageToken']
                )
                response = request.execute()
                process_replies(response['items'])
    
    return comments

def comment_threads(id, ep_no, is_last, part_no):
    # get video name
    request = YOUTUBE.videos().list(part='snippet', id=id)
    response = request.execute()
    video_name = response['items'][0]['snippet']['title']
    video_name = re.sub('[\/:*?"<>|]', '', video_name)
    print(f'Fetching comments from ep. {ep_no}:{video_name}')
    
    # get initial comments
    comments_list = []
    request = YOUTUBE.commentThreads().list(
        part='snippet,replies',
        videoId=id,
        maxResults=100
    )
    response = request.execute()
    comments_list.extend(process_comments(response['items']))

    # get the rest of the comments
    while response.get('nextPageToken', None):
        request = YOUTUBE.commentThreads().list(
            part='snippet,replies',
            videoId=id,
            maxResults=100,
            pageToken=response['nextPageToken']
        )
        response = request.execute()
        comments_list = process_comments(response['items'])
    
    if (is_last):
        with open(f'./datasets/hologra_comments_{part_no}.csv', 'w', encoding='utf8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=comments_list[0].keys(), escapechar='\\')
            writer.writeheader()
            writer.writerows(comments_list)

        print(f'Done. {len(comments_list)} comments fetched.')
        print(f'Time took: {round(time.time() - START_TIME, 2)} seconds.')

if __name__ == '__main__':
    # ids separated into parts in order to not overload daily quota limit
    part_1 = [['3', 'UVncAW3h45E'],  ['5', 'wj9GO6F0pOM'],  ['8', 'xHWN_nIHbU8'],  ['9', 'fzIeI3YjWAI'],  ['11', '4nE1Q_lawyw'],
              ['12', 'Yprgi11h0sk'], ['14', 'ycxDOZOgnTY'], ['15', 'a7HTAa-iR9k'], ['17', 'v8siufikYPg'], ['18', 'O-SXhtYjprc'],
              ['20', '4l1jdGILjPw'], ['21', '7v1rw3kL89M'], ['23', 'jnruFkwWZDU'], ['25', 'KjARsYeUq1Q'], ['26', 'XIli-chomNk'],
              ['28', 'fUdHLOxz3GM'], ['31', 'eA268DT2BvY'], ['32', 'GiCzxT2j7yk'], ['34', 'MuliaE83B_I'], ['35', 'ebyp__4vy10'],
              ['36', '3dG5xMBXdwI'], ['37', 'tMqcIXNtdh8'], ['40', 'vPgie-tpVHU'], ['41', 'saPtg9fdWYg'], ['42', '9-cmxJQG4t4'],
              ['43', 'vT19X_tTM2U'], ['44', '_B-Q10J9KSg']]
              
    part_2 = [['52', 'Cgf-qkaDZAU'], ['55', 'iGNBjxe7_2g'], ['56', 'PJf3XZ636-0'], ['57', 'hnAGiLD8hEY'], ['58', 'hUCoGATqHNU'],
              ['59', 'q-MzByHv7GY'], ['60', 'MBbOFD2lOoo'], ['61', 'NU4RAfwXL8Q'], ['62', 'd2EAL9seVK4'], ['63', '3IuYMr-41bM'],
              ['64', 'o3tp4kQ081E'], ['65', 'dMAyQAiv8MQ'], ['66', 'KSgTX0YF5NY'], ['67', '_GlqT6O0UVo'], ['68', '8GLSHHLP91s'],
              ['69', '4MJQxT5-Zhc'], ['70', 'vVDcEsz5k_Q'], ['71', 'TlH0in-TEFI'], ['72', 'Pa10pmlbXB4'], ['73', 'YpTAqjljvzg'],
              ['74', 'IB-41BrvMfI'], ['75', 'p554IIGY8Dw'], ['76', 'zzoZr-dNlks'], ['77', 'ob_atuYtldQ'], ['78', '7FDwTV2AanI'],
              ['79', 'Mbf2qj8Amxg'], ['80', '-IYGrFsXguc'], ['81', 'hlH6iNcEvq8'], ['82', 'y0yB6bXuf1E'], ['83', 'ljZwKRVrMps'],
              ['84', 'a8CK7s_VZvo'], ['85', 'UFzZbd-O1MQ'], ['86', 'NL-WJy8THpA'], ['87', 'i_9xsmRez4Y'], ['88', 'sif0cB8BnS8'],
              ['89', 'KAbjx24XbCs'], ['90', 'uhbGec_6mfQ'], ['91', 'lz08zMLUtEc'], ['92', 'Acw8qh9lOGU'], ['93', '2wOBwf_vsTw'],
              ['94', '6NSdYeW4cRc'], ['95', 'CGUIL02BtQs'], ['96', 'u-Fvkyp8I4c'], ['97', 'ChEu7qkztNg'], ['98', '4zlFqLoErkk'],
              ['99', 'VopFRgAJo_I'], ['100', 'Hs5wAN_AeBo']]
           
    part_3 = [['101', 'IeWMT2PVhE0'], ['102', 'dr0yef-9WOU'], ['103', 'oWh7ux1P3kw'], ['104', '05VuFmvHjNY'], ['105', 'vARkqQEFR-s'],
              ['106', 'IVnnd0lNRtM'], ['107', 'r-Va_SVWRP4'], ['108', 'wc6V5lQV6eU'], ['109', 'ZWTuQnb9wq0'], ['110', 'gDRqKpsO8xg'],
              ['111', 'z9tM83LrJEM'], ['112', 'sTbr9DiQxJ4'], ['113', '_JxbqVD1AQU'], ['114', 'RzOq4iCzZ9M'], ['115', 'IVxllrBa6ek'],
              ['116', 'gvRPXNAKUp8'], ['117', '6HI6L2Y2Ry4'], ['118', '9nQurjU-Ky0'], ['119', '0g2lalD4Lqc'], ['120', 'vF2-vhOkYLs'],
              ['121', 'KCyeZFxrYKs'], ['122', 'OaSWjqa5uYA'], ['123', 'zsia2JWuMso'], ['124', 'xenG9OdpMcg'], ['125', 'M23vq8vx9ZM'],
              ['126', 'OB2HUC22aHo'], ['127', 'fvZR8Hy8WGM'], ['128', '0IT4AlfL7wU'], ['129', 'VcWZ4njr4ew'], ['130', 'rKW_bg3DkLM'],
              ['131', 'liKwZRcIlJw'], ['132', 'GG-fPw4kYN0'], ['133', 'd2_t3YWuxJc'], ['134', '_scyoAqKG9E'], ['135', 'm8Y5j82i9TY'],
              ['136', '7oyT4JuuGf4'], ['137', 'O775092N3nU'], ['138', 'bx0hSfF2v2U'], ['139', 'QbwQaCozLxo'], ['140', 'Ez2n-qKqrxc'],
              ['141', 'pjDqJJePGQg'], ['142', 'D_bKO48KyX4'], ['143', '-1yyK5E7v_A'], ['144', 'DAYQIUScsPU'], ['145', 'T0dml5y2jZ4'],
              ['146', '6Li1JW3URWQ'], ['147', 'fBpnJQdDlog'], ['148', 'TheM-kB2fXE'], ['149', 'vaKSDxyIcj8'], ['150', 'aBlUC-0pdwc']]
              
    part_4 = [['151', 'x-_rBrnQesY'], ['152', 'RPfntreemLs'], ['153', '3Bmzo_7w2_U'], ['154', 'qdaeGH3fJZo'], ['155', 'UorTPrd0Mlg'],
              ['156', 'LVYMEKlSelU'], ['157', 'A5rX7aGGDIU'], ['158', 'H_nFL4h4ojU'], ['159', 'NTaPIQ7iPmg'], ['160', 'ldnAEpMi2EY'],
              ['161', '3ic4KSFjdAU'], ['162', 'ddiqpbfrgwo'], ['163', '8d4LnRn1jds'], ['164', 'wN6FAJVmwXE'], ['165', 'tu7qKF8x1Po'],
              ['166', 'gFfL_Wl0TPQ'], ['167', 'elvsgZ06ksc'], ['168', '1YEY0_uoXCI'], ['169', 'B4A7Peur5Vs'], ['170', 'xjd_WW3MBow']]
              
    # manually change variables accordingly
    for i in range(len(part_4)):
        comment_threads(part_4[i][1], part_4[i][0], i == len(part_4) - 1, 'part_4')

#         length comments
# part_1  27     48232
# part_2  47     198901
# part_3  50     201749
# part_4  20     58295
# total   144    507177