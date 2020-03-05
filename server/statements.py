class Statement:

	def __init__(self, msg_type, pre, folder, anim, msg, pos, sfx, anim_type, cid, sfx_delay, button, evidence, flip, ding, color, showname, charid_pair, other_folder, other_emote, offset_pair, other_offset, other_flip, nonint_pre):
		self.msg_type = msg_type
		self.pre = pre
		self.folder = folder
		self.anim = anim
		self.msg = msg
		self.pos = pos
		self.sfx = sfx
		self.anim_type = anim_type
		self.cid = cid
		self.sfx_delay = sfx_delay
		self.button = button
		self.evidence = evidence
		self.flip = flip
		self.ding = ding
		self.color = color
		self.showname = showname
		self.charid_pair = charid_pair
		self.other_folder = other_folder
		self.other_emote = other_emote
		self.offset_pair = offset_pair
		self.other_offset = other_offset
		self.other_flip = other_flip
		self.nonint_pre = nonint_pre

		self.id = 0