from hands_detection import HandsDetection
from pose_detection import PoseDetection
from holistic_detection import HolisticDetection
def main():
    while True:
        choise_input = int(input("1:Hands Detection, 2:Pose Detection, 3:Holistic Detection =>"))
        if choise_input == '1':
            detector = HandsDetection()
            break

        elif choise_input == '2':
            detector = PoseDetection()
            break

        elif choise_input == '3':
            detector = HolisticDetection()
            break
        else:
            print('Tekrar input gir lütfen!')
            return
if __name__ == '__main__':
    main()

