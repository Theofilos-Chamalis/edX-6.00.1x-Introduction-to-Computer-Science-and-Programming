class Member(object):
    def __init__(self, founder):
        """ 
        founder: string
        Initializes a member. 
        Name is the string of name of this node,
        parent is None, and no children
        """        
        self.name = founder
        self.parent = None         
        self.children = []    

    def __str__(self):
        return self.name    

    def add_parent(self, mother):
        """
        mother: Member
        Sets the parent of this node to the `mother` Member node
        """
        self.parent = mother   

    def get_parent(self):
        """
        Returns the parent Member node of this Member
        """
        return self.parent 

    def is_parent(self, mother):
        """
        mother: Member
        Returns: Boolean, whether or not `mother` is the 
        parent of this Member
        """
        return self.parent == mother  

    def add_child(self, child):
        """
        child: Member
        Adds another child Member node to this Member
        """
        self.children.append(child)   

    def is_child(self, child):
        """
        child: Member
        Returns: Boolean, whether or not `child` is a
        child of this Member
        """
        return child in self.children


class Family(object):
    def __init__(self, founder):
        """ 
        Initialize with string of name of oldest ancestor

        Keyword arguments:
        founder -- string of name of oldest ancestor
        """

        self.names_to_nodes = {}
        self.root = Member(founder)    
        self.names_to_nodes[founder] = self.root   

    def set_children(self, mother, list_of_children):
        """
        Set all children of the mother. 

        Keyword arguments: 
        mother -- mother's name as a string
        list_of_children -- children names as strings
        """
        # convert name to Member node (should check for validity)
        mom_node = self.names_to_nodes[mother]   
        # add each child
        for c in list_of_children:           
            # create Member node for a child   
            c_member = Member(c)               
            # remember its name to node mapping
            self.names_to_nodes[c] = c_member    
            # set child's parent
            c_member.add_parent(mom_node)        
            # set the parent's child
            mom_node.add_child(c_member)         
    
    def is_parent(self, mother, kid):
        """
        Returns True or False whether mother is parent of kid. 

        Keyword arguments: 
        mother -- string of mother's name
        kid -- string of kid's name
        """
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)   

    def is_child(self, kid, mother):
        """
        Returns True or False whether kid is child of mother. 

        Keyword arguments: 
        kid -- string of kid's name
        mother -- string of mother's name
        """        
        mom_node = self.names_to_nodes[mother]   
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)

    def cousin(self, a, b):
        """
        Returns a tuple of (the cousin type, degree removed) 

        cousin type is an integer that is -1 if a and b
        are the same node or if one is the direct descendent 
        of the other.  Otherwise, cousin type is 0 or greater,
        representing the shorter distance to their common 
        ancestor as described in 5-2.

        degree removed is the distance to the common ancestor

        Keyword arguments: 
        a -- string that is the name of a
        b -- string that is the name of b
        """
        if a == b:
            return (-1,0)
        a = self.names_to_nodes[a]
        b = self.names_to_nodes[b]
        if a.is_parent(b) or b.is_parent(a):
            return (-1,0)
        ParentA = a
        ParentB = b        
        glA = 0
        glB = 0
        removed = 0
        cType = -1
        while(ParentA.get_parent() != None):
            glA += 1
            ParentA = ParentA.get_parent()
        while(ParentB.get_parent() != None):
            glB += 1
            ParentB = ParentB.get_parent()

        if( glA > glB):
            removed = glA-glB
        if( glA < glB):
            removed = glB-glA
        ParentA=a
        ParentB=b
        if( glA > glB+1):
            for i in range(glA-glB-1):
                ParentA = ParentA.get_parent()
        elif(glB > glA+1):      #jezeli roznica ich pokrewienstwa jest wieksza od 1
            for i in range(glB-glA-1):
                ParentB = ParentB.get_parent()       #zmniejsz ja do 1
        elif(glA == glB):    #jezeli sa na tym samym poziomie
            ParentA = a.get_parent()     # zmien ten poziom
            cType = 0
        if(glA > glB):
            while ParentA.is_parent(ParentB)==False:
                ParentA = ParentA.get_parent()
                ParentB = ParentB.get_parent()
                cType += 1
            return (cType, removed)
        else:
            while ParentB.is_parent(ParentA) == False:
                ParentA = ParentA.get_parent()
                ParentB = ParentB.get_parent()
                cType += 1
            return (cType, removed)