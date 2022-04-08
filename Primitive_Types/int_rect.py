#write a program which tests if two rectangles have a non empty intersection
# book hint: think of the X and Y dimensions independently 
# according to the book, the problem is unspecified enough 
# so that we can also take into account the border of the rectangle
# in otherwords, two rectangles with touching corners is enough to count as "intersecting"
# good book approach:
# focus on conditions where the rectangles are guaranteed NOT intersecting 
# another way to think about it 
# if the range of the X / Y-values of the rectangles do not intersect
# alternatively if X's and Y's intersect the book explains -> "all X and Y values 
# are common to the two rectangles so there is a  nonempty intersection "
# 
# 
# #

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))

def intersect_rectangle(R1, R2):
    def is_intersecting(R1, R2):
        return ( R1.x <= R2.x + R2.width 
        and R1.x + R1.width >= R2.x 
        and R1.y <= R2.y + R2.height
        and R1.y + R1.height >= R2.y)

    if not is_intersecting(R1, R2):
        return(0 , 0 , -1, -1)
    return Rectangle(
        max(R1.x , R2.x),
        max(R1.y , R2.y),
        min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x),
        min(R1.y + R1.height , R2.y + R2.height) - max(R1.y, R2.y)
    )