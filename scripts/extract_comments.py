from googleapiclient.discovery import build
from dotenv import load_dotenv
from time import perf_counter
import pandas as pd
import os, re

def main(episode):
    ep_no = episode[0]
    id = episode[1]
    progress = 0
    # get video details
    video_request = youtube.videos().list(part='snippet,statistics', id=id)
    video_response = video_request.execute()
    video_name = re.sub('[\/:*?"<>|]', '', video_response['items'][0]['snippet']['title'])
    video_comment_count = video_response['items'][0]['statistics']['commentCount']
    print(f'{ep_no}:{video_name}')

    # get comments
    comment_request = youtube.commentThreads().list(
        part='snippet,replies',
        videoId=id,
        maxResults=100
    )
    while comment_request is not None:
        comment_response = comment_request.execute()

        for item in comment_response['items']:
            comments.append(item['snippet']['topLevelComment']['snippet']['textOriginal'])
            
            # get replies if present
            if 'replies' in item.keys():
                reply_request = youtube.comments().list(
                    part='snippet',
                    parentId=item['snippet']['topLevelComment']['id'],
                    maxResults=100
                )
                while reply_request is not None:
                    reply_response = reply_request.execute()

                    for item in reply_response['items']:
                        comments.append(item['snippet']['textOriginal'])

                        progress += 1
                        print(f'{progress}/{video_comment_count}', end='\r')

                    reply_request = youtube.comments().list_next(reply_request, reply_response)
            
            progress += 1
            print(f'{progress}/{video_comment_count}', end='\r')

            comment_request = youtube.commentThreads().list_next(comment_request, comment_response)

if __name__ == '__main__':
    load_dotenv()
    youtube = build('youtube', 'v3', developerKey=os.getenv('API_KEY'))
    # ids separated into parts in order to not overload daily quota limit
    part_1 = [['3',  'UVncAW3h45E'], ['5',  'wj9GO6F0pOM'], ['8',  'xHWN_nIHbU8'], ['9',  'fzIeI3YjWAI'], ['11', '4nE1Q_lawyw'],
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
              ['166', 'gFfL_Wl0TPQ'], ['167', 'elvsgZ06ksc'], ['168', '1YEY0_uoXCI'], ['169', 'B4A7Peur5Vs'], ['170', 'xjd_WW3MBow'], 
              ['171', 'G7McWcwSPUU'], ['172', 'Wrpz5U6eO78'], ['173', 'iKh8QaAJHcw'], ['174', 'PQ3--0NvUa8'], ['175', 'QWlxvSWIt7w'], 
              ['176', 'RSi00fM6ryg'], ['177', '1u_vxV0Gq4w'], ['178', '79FenFDB_bI'], ['179', 'kvvV5iBtuFk'], ['180', 'fQ5hbR4H4wg'], 
              ['181', 'SYkJ9U6NCOo'], ['182', '4kmdCxIm0E8'], ['183', 'h14QJuq9z_Y'], ['184', 'rZ4r_b4a7OY'], ['185', '8feDwm0ylbQ'], 
              ['186', 'dT2Wua-2RIU'], ['187', 'm300EONBDTw'], ['188', 'ExRYtdoeUrY'], ['189', 'z49KF-GwY-4'], ['190', '-_VzPpAl_94'], 
              ['191', 'VbkGgTxEEeA'], ['192', 'PQ54uUV41-k'], ['193', 'LCb66ERHUEc'], ['194', 'dQFNmc-OoVM'], ['195', '2mQFojrPOSI'], 
              ['196', 'U1N_MbbkBiU'], ['197', 'yEsX4I6ZwFA'], ['198', '7Z_OVu1vxrQ'], ['199', '8m43v6CX6hM'], ['200', '2gC-m5rfmIU']]
    
    start = perf_counter()
    comments = []
    # manually change variables accordingly
    for episode in part_4:
        main(episode)

    df = pd.DataFrame({'comment': comments})
    df.to_csv('./datasets/hologra_comments_part_4.csv', index=None)
    print(f'Done. Time took: {round(perf_counter() - start, 2)} seconds.')
    print(f'Length: {len(df)}')

#         length comments
# part_1  27     48232
# part_2  47     198901
# part_3  50     201749
# part_4  50     123763
# total   144    507177